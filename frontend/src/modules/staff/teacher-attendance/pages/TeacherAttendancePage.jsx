// ============================================
// TEACHER ATTENDANCE PAGE
// File: TeacherAttendancePage.jsx
// ============================================

import { useEffect, useMemo, useState } from "react";
import toast from "react-hot-toast";
import teacherAttendanceService from "../services/teacherAttendanceService";

const STATUS_OPTIONS = [
  { value: "PRESENT", label: "Present" },
  { value: "ABSENT", label: "Absent" },
  { value: "LEAVE", label: "Leave" },
  { value: "HALF_DAY", label: "Half Day" },
  { value: "OFFICIAL_DUTY", label: "Official Duty" },
];

const TeacherAttendancePage = () => {
  // ============================================
  // TODAY
  // ============================================
  const today = new Date().toISOString().split("T")[0];

  // ============================================
  // STATE
  // ============================================
  const [attendanceDate, setAttendanceDate] = useState(today);
  const [attendance, setAttendance] = useState([]);
  const [loading, setLoading] = useState(false);
  const [search, setSearch] = useState("");

  // ============================================
  // LOAD ATTENDANCE
  // ============================================
  const loadAttendance = async () => {
    try {
      setLoading(true);
      const response = await teacherAttendanceService.getTeacherAttendance(attendanceDate);
      setAttendance(response.teachers || []);
    } catch (error) {
      console.error(error);
      toast.error("Unable to load attendance.");
    } finally {
      setLoading(false);
    }
  };

  // ============================================
  // LOAD ON DATE CHANGE
  // ============================================
  useEffect(() => {
    loadAttendance();
  }, [attendanceDate]);

  // ============================================
  // UPDATE STATUS
  // ============================================
  const handleStatusChange = (teacherId, status) => {
    setAttendance(
      attendance.map((item) =>
        item.teacher === teacherId ? { ...item, status } : item
      )
    );
  };

  // ============================================
  // UPDATE REMARKS
  // ============================================
  const handleCheckInChange = (teacherId, value) => {
    setAttendance(
      attendance.map((item) =>
        item.teacher === teacherId
          ? { ...item, check_in: value }
          : item
      )
    );
  };

  const handleCheckOutChange = (teacherId, value) => {
    setAttendance(
      attendance.map((item) =>
        item.teacher === teacherId
          ? { ...item, check_out: value }
          : item
      )
    );
  };

  const handleRemarksChange = (teacherId, remarks) => {
    setAttendance(
      attendance.map((item) =>
        item.teacher === teacherId ? { ...item, remarks } : item
      )
    );
  };

  // ============================================
  // MARK ALL PRESENT
  // ============================================
  const markAllPresent = () => {
    setAttendance(
      attendance.map((item) => ({
        ...item,
        status: "PRESENT",
      }))
    );
    toast.success("All teachers marked Present.");
  };

  // ============================================
  // SEARCH FILTER
  // ============================================
  const filteredAttendance = useMemo(() => {
    const keyword = search.toLowerCase();
    return attendance.filter(
      (item) =>
        item.teacher_name?.toLowerCase().includes(keyword) ||
        item.employee_id?.toLowerCase().includes(keyword) ||
        item.post_type?.toLowerCase().includes(keyword)
    );
  }, [attendance, search]);

  // ============================================
  // SUMMARY
  // ============================================
  const summary = useMemo(() => {
    return {
      total: attendance.length,
      present: attendance.filter((x) => x.status === "PRESENT").length,
      absent: attendance.filter((x) => x.status === "ABSENT").length,
      leave: attendance.filter((x) => x.status === "LEAVE").length,
      halfDay: attendance.filter((x) => x.status === "HALF_DAY").length,
      officialDuty: attendance.filter((x) => x.status === "OFFICIAL_DUTY").length,
    };
  }, [attendance]);

  // ============================================
  // SAVE
  // ============================================
  const handleSave = async () => {
    try {
      setLoading(true);
      await teacherAttendanceService.saveTeacherAttendance({
        date: attendanceDate,
        attendance: attendance.map((item) => ({
          teacher: item.teacher,
          status: item.status,
          remarks: item.remarks,
          check_in: item.check_in,
          check_out: item.check_out,
        })),
      });
      toast.success("Attendance saved successfully.");
    } catch (error) {
      console.error(error);
      toast.error("Failed to save attendance.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* ============================================
          PAGE HEADER
      ============================================ */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Teacher Attendance
          </h1>
          <p className="text-gray-500 mt-1">
            Mark daily attendance for all teachers.
          </p>
        </div>
        <button
          onClick={handleSave}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl disabled:opacity-50"
        >
          {loading ? "Saving..." : "Save Attendance"}
        </button>
      </div>

      {/* ============================================
          FILTERS
      ============================================ */}
      <div className="bg-white rounded-xl shadow p-5">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {/* DATE */}
          <div>
            <label className="block mb-2 font-medium">
              Attendance Date
            </label>
            <input
              type="date"
              value={attendanceDate}
              onChange={(e) => setAttendanceDate(e.target.value)}
              className="w-full border rounded-lg px-4 py-2"
            />
          </div>

          {/* SEARCH */}
          <div>
            <label className="block mb-2 font-medium">
              Search Teacher
            </label>
            <input
              type="text"
              value={search}
              placeholder="Employee ID / Teacher Name"
              onChange={(e) => setSearch(e.target.value)}
              className="w-full border rounded-lg px-4 py-2"
            />
          </div>

          {/* BUTTON */}
          <div className="flex items-end">
            <button
              onClick={markAllPresent}
              className="bg-green-600 hover:bg-green-700 text-white px-5 py-2 rounded-lg"
            >
              Mark All Present
            </button>
          </div>
        </div>
      </div>

      {/* ============================================
          SUMMARY
      ============================================ */}
      <div className="grid grid-cols-2 md:grid-cols-6 gap-4">
        <div className="bg-blue-50 rounded-xl p-4">
          <p className="text-sm text-gray-500">Total</p>
          <h2 className="text-3xl font-bold">{summary.total}</h2>
        </div>
        <div className="bg-green-50 rounded-xl p-4">
          <p className="text-sm text-gray-500">Present</p>
          <h2 className="text-3xl font-bold text-green-700">{summary.present}</h2>
        </div>
        <div className="bg-red-50 rounded-xl p-4">
          <p className="text-sm text-gray-500">Absent</p>
          <h2 className="text-3xl font-bold text-red-700">{summary.absent}</h2>
        </div>
        <div className="bg-yellow-50 rounded-xl p-4">
          <p className="text-sm text-gray-500">Leave</p>
          <h2 className="text-3xl font-bold text-yellow-700">{summary.leave}</h2>
        </div>
        <div className="bg-orange-50 rounded-xl p-4">
          <p className="text-sm text-gray-500">Half Day</p>
          <h2 className="text-3xl font-bold text-orange-700">{summary.halfDay}</h2>
        </div>
        <div className="bg-purple-50 rounded-xl p-4">
          <p className="text-sm text-gray-500">Official Duty</p>
          <h2 className="text-3xl font-bold text-purple-700">{summary.officialDuty}</h2>
        </div>
      </div>

      {/* ============================================
          ATTENDANCE TABLE
      ============================================ */}
      <div className="bg-white rounded-xl shadow overflow-x-auto">
        <table className="min-w-full text-sm">
          <thead className="bg-gray-100">
            <tr>
              <th className="p-3 text-left">#</th>
              <th className="text-left">Employee ID</th>
              <th className="text-left">Teacher</th>
              <th className="text-left">Post</th>
              <th className="text-center">Status</th>
              <th className="text-center">Check In</th>
              <th className="text-center">Check Out</th>
              <th className="text-left">Remarks</th>
            </tr>
          </thead>
          <tbody>
            {filteredAttendance.length > 0 ? (
              filteredAttendance.map((teacher, index) => (
                <tr key={teacher.teacher} className="border-b hover:bg-gray-50">
                  {/* SR NO */}
                  <td className="p-3">{index + 1}</td>

                  {/* EMPLOYEE ID */}
                  <td>{teacher.employee_id}</td>

                  {/* TEACHER NAME */}
                  <td>
                    <div className="font-medium">{teacher.teacher_name}</div>
                  </td>

                  {/* POST */}
                  <td>{teacher.post_type}</td>

                  {/* STATUS */}
                  <td className="text-center">
                    <select
                      value={teacher.status}
                      onChange={(e) =>
                        handleStatusChange(teacher.teacher, e.target.value)
                      }
                      className="border rounded-lg px-3 py-2 w-40"
                    >
                      {STATUS_OPTIONS.map((status) => (
                        <option key={status.value} value={status.value}>
                          {status.label}
                        </option>
                      ))}
                    </select>
                  </td>

                  <td>
                    <input
                      type="time"
                      value={teacher.check_in || ""}
                      onChange={(e) =>
                        handleCheckInChange(teacher.teacher, e.target.value)
                      }
                      className="border rounded-lg px-2 py-2"
                    />
                  </td>

                  <td>
                    <input
                      type="time"
                      value={teacher.check_out || ""}
                      onChange={(e) =>
                        handleCheckOutChange(teacher.teacher, e.target.value)
                      }
                      className="border rounded-lg px-2 py-2"
                    />
                  </td>

                  {/* REMARKS */}
                  <td>
                    <input
                      type="text"
                      value={teacher.remarks || ""}
                      onChange={(e) =>
                        handleRemarksChange(teacher.teacher, e.target.value)
                      }
                      placeholder="Remarks"
                      className="w-full border rounded-lg px-3 py-2"
                    />
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="8" className="text-center py-10 text-gray-500">
                  No teachers found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* ============================================
          FOOTER
      ============================================ */}
      <div className="flex justify-between items-center bg-white rounded-xl shadow p-4">
        <div className="text-sm text-gray-500">
          Showing <span className="font-semibold"> {filteredAttendance.length} </span> teacher(s)
        </div>
        <button
          onClick={handleSave}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-xl disabled:opacity-50"
        >
          {loading ? "Saving..." : "Save Attendance"}
        </button>
      </div>
    </div>
  );
};

export default TeacherAttendancePage;