import React, { useState, useEffect, useCallback, useMemo } from "react";
import subjectRequirementService from "../services/subjectRequirementService";

// IMPORTANT: You will need to import your actual services for fetching Classes and Subjects
// import classService from "../../../../services/api/classService";
// import subjectService from "../../../../services/api/subjectService";

const SubjectRequirementMatrixPage = () => {
  const [existingRequirements, setExistingRequirements] = useState([]);
  const [classes, setClasses] = useState([]);
  const [subjects, setSubjects] = useState([]);
  
  const [matrixData, setMatrixData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);

  // 1. Fetch All Required Data
  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      // Replace the empty arrays below with your actual API calls
      // const [reqRes, classRes, subjectRes] = await Promise.all([
      //   subjectRequirementService.getAll(),
      //   classService.getAll(),
      //   subjectService.getAll()
      // ]);

      // Mocking the API calls for demonstration. Wire this up to your real endpoints.
      const reqRes = await subjectRequirementService.getAll().catch(() => ({ data: { results: [] } }));
      
      // MOCK DATA: Remove this once you wire up your classService and subjectService
      const classRes = { data: { results: [{ id: 1, name: "11TH" }, { id: 2, name: "12TH" }] } };
      const subjectRes = { data: { results: [{ id: 101, name: "Physics" }, { id: 102, name: "Chemistry" }] } };

      const fetchedRequirements = reqRes.data?.results || reqRes.data || [];
      const fetchedClasses = classRes.data?.results || classRes.data || [];
      const fetchedSubjects = subjectRes.data?.results || subjectRes.data || [];

      setExistingRequirements(fetchedRequirements);
      setClasses(fetchedClasses);
      setSubjects(fetchedSubjects);

      // 2. Build the Matrix
      buildMatrix(fetchedClasses, fetchedSubjects, fetchedRequirements);
    } catch (err) {
      setError("Failed to load data. Please check your network or server.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  // 3. Generate rows for every Class + Subject combination
  const buildMatrix = (classList, subjectList, requirements) => {
    let newMatrix = [];

    classList.forEach((schoolClass) => {
      subjectList.forEach((subject) => {
        // Check if this combination already exists in the database
        const existing = requirements.find(
          (req) => req.school_class === schoolClass.id && req.subject === subject.id
        );

        if (existing) {
          newMatrix.push({ ...existing }); // Use existing data
        } else {
          // Create a blank row for the user to fill out
          newMatrix.push({
            id: null, // Null ID means it will be created on Bulk Save
            school_class: schoolClass.id,
            school_class_name: schoolClass.name,
            subject: subject.id,
            subject_name: subject.name,
            stream: null,
            stream_name: "-",
            theory_periods_per_week: 0,
            lab_periods_per_week: 0,
            teachers_required: 1,
            priority: 0,
            is_compulsory: false,
            is_active: true,
          });
        }
      });
    });

    setMatrixData(newMatrix);
  };

  // Handle Input Changes
  const handleCellChange = (index, field, value) => {
    setMatrixData((prev) => {
      const updated = [...prev];
      updated[index] = { ...updated[index], [field]: value };
      return updated;
    });
  };

  // Submit Changes
  const handleBulkSave = async () => {
    setSaving(true);
    setError(null);
    setSuccessMessage(null);
    
    // Only send rows where periods > 0 or it already has an ID (meaning we are updating it)
    const rowsToSave = matrixData.filter(
      row => row.id || row.theory_periods_per_week > 0 || row.lab_periods_per_week > 0
    );

    try {
      const response = await subjectRequirementService.bulkSave(rowsToSave);
      setSuccessMessage(`Successfully saved ${response.data.count} requirements.`);
      fetchData(); // Refresh the grid to get actual IDs from the database
    } catch (err) {
      setError(err.response?.data?.detail || "Save failed. Please check your inputs.");
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div style={styles.loadingContainer}>
        <div style={styles.spinner}></div>
        <p>Loading Matrix Data...</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h2 style={styles.title}>Subject Requirement Matrix</h2>
        <div style={styles.actions}>
          <button onClick={fetchData} style={styles.btnSecondary} disabled={saving}>
            Refresh
          </button>
          <button style={styles.btnSecondary} disabled={saving}>
            Export Excel
          </button>
          <button onClick={handleBulkSave} disabled={saving} style={styles.btnPrimary}>
            {saving ? "Saving..." : "Bulk Save Changes"}
          </button>
        </div>
      </header>

      {error && <div style={styles.errorBanner}>{error}</div>}
      {successMessage && <div style={styles.successBanner}>{successMessage}</div>}

      <div style={styles.tableWrapper}>
        <table style={styles.table}>
          <thead>
            <tr>
              <th style={styles.th}>Class</th>
              <th style={styles.th}>Stream</th>
              <th style={styles.th}>Subject</th>
              <th style={styles.th}>Theory Periods</th>
              <th style={styles.th}>Lab Periods</th>
              <th style={styles.th}>Teachers Req.</th>
              <th style={styles.th}>Priority</th>
              <th style={styles.th}>Compulsory?</th>
              <th style={styles.th}>Active?</th>
            </tr>
          </thead>
          <tbody>
            {matrixData.length === 0 ? (
              <tr>
                <td colSpan="9" style={styles.emptyState}>No classes or subjects found.</td>
              </tr>
            ) : (
              matrixData.map((row, index) => {
                // Determine if this row represents a new class group to add a subtle visual separator
                const isNewGroup = index > 0 && matrixData[index - 1].school_class !== row.school_class;
                const trStyle = isNewGroup ? { ...styles.tr, borderTop: "2px solid #cbd5e1" } : styles.tr;

                return (
                  <tr key={`${row.school_class}-${row.subject}`} style={trStyle}>
                    <td style={styles.td}><strong>{row.school_class_name}</strong></td>
                    <td style={styles.td}>{row.stream_name || "-"}</td>
                    <td style={styles.td}>{row.subject_name}</td>
                    
                    <td style={styles.td}>
                      <input
                        type="number" min="0" value={row.theory_periods_per_week || 0}
                        onChange={(e) => handleCellChange(index, "theory_periods_per_week", parseInt(e.target.value) || 0)}
                        style={styles.input}
                      />
                    </td>
                    <td style={styles.td}>
                      <input
                        type="number" min="0" value={row.lab_periods_per_week || 0}
                        onChange={(e) => handleCellChange(index, "lab_periods_per_week", parseInt(e.target.value) || 0)}
                        style={styles.input}
                      />
                    </td>
                    <td style={styles.td}>
                      <input
                        type="number" min="1" value={row.teachers_required || 1}
                        onChange={(e) => handleCellChange(index, "teachers_required", parseInt(e.target.value) || 1)}
                        style={styles.input}
                      />
                    </td>
                    <td style={styles.td}>
                      <input
                        type="number" min="0" value={row.priority || 0}
                        onChange={(e) => handleCellChange(index, "priority", parseInt(e.target.value) || 0)}
                        style={styles.input}
                      />
                    </td>
                    <td style={styles.td}>
                      <input
                        type="checkbox" checked={row.is_compulsory || false}
                        onChange={(e) => handleCellChange(index, "is_compulsory", e.target.checked)}
                        style={styles.checkbox}
                      />
                    </td>
                    <td style={styles.td}>
                      <input
                        type="checkbox" checked={row.is_active || false}
                        onChange={(e) => handleCellChange(index, "is_active", e.target.checked)}
                        style={styles.checkbox}
                      />
                    </td>
                  </tr>
                );
              })
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

// Professional Styling 
const styles = {
  container: { padding: "24px", fontFamily: "system-ui, -apple-system, sans-serif", backgroundColor: "#f8fafc", minHeight: "100vh" },
  header: { display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "24px" },
  title: { margin: 0, fontSize: "24px", color: "#0f172a", fontWeight: "600" },
  actions: { display: "flex", gap: "12px" },
  btnPrimary: { backgroundColor: "#10b981", color: "white", padding: "10px 20px", borderRadius: "6px", border: "none", fontWeight: "600", cursor: "pointer", transition: "all 0.2s" },
  btnSecondary: { backgroundColor: "white", color: "#475569", padding: "10px 20px", borderRadius: "6px", border: "1px solid #cbd5e1", fontWeight: "500", cursor: "pointer", transition: "all 0.2s" },
  errorBanner: { backgroundColor: "#fee2e2", color: "#991b1b", padding: "16px", borderRadius: "6px", marginBottom: "20px", borderLeft: "4px solid #ef4444" },
  successBanner: { backgroundColor: "#dcfce3", color: "#166534", padding: "16px", borderRadius: "6px", marginBottom: "20px", borderLeft: "4px solid #22c55e" },
  tableWrapper: { backgroundColor: "white", borderRadius: "8px", border: "1px solid #e2e8f0", overflowX: "auto", boxShadow: "0 1px 3px 0 rgba(0, 0, 0, 0.1)" },
  table: { width: "100%", borderCollapse: "collapse", textAlign: "left", whiteSpace: "nowrap" },
  th: { padding: "16px", backgroundColor: "#f1f5f9", color: "#334155", fontWeight: "600", fontSize: "14px", borderBottom: "1px solid #e2e8f0", position: "sticky", top: 0, zIndex: 10 },
  tr: { borderBottom: "1px solid #e2e8f0", transition: "background-color 0.1s" },
  td: { padding: "12px 16px", color: "#475569", fontSize: "14px" },
  input: { width: "70px", padding: "8px", borderRadius: "4px", border: "1px solid #cbd5e1", fontSize: "14px", outline: "none", transition: "border-color 0.2s" },
  checkbox: { width: "18px", height: "18px", accentColor: "#10b981", cursor: "pointer" },
  emptyState: { textAlign: "center", padding: "48px", color: "#64748b" },
  loadingContainer: { display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "50vh", color: "#64748b" },
  spinner: { width: "40px", height: "40px", border: "4px solid #e2e8f0", borderTop: "4px solid #10b981", borderRadius: "50%", animation: "spin 1s linear infinite", marginBottom: "16px" }
};

export default SubjectRequirementMatrixPage;