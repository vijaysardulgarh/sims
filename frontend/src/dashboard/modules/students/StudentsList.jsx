import { useState } from "react";

import { useNavigate } from "react-router-dom";

import DataTable from "../../components/crud/DataTable";
import SearchBox from "../../components/crud/SearchBox";
import Pagination from "../../components/crud/Pagination";
import ImportButton from "../../components/crud/ImportButton";
import ExportButton from "../../components/crud/ExportButton";

const StudentsList = () => {

  // =========================
  // NAVIGATION
  // =========================

  const navigate = useNavigate();

  // =========================
  // STUDENTS STATE
  // =========================

  const [students, setStudents] = useState([
    {
      id: 1,
      admissionNo: "SIMS001",
      name: "Rahul Sharma",
      class: "10",
      section: "A",
      status: "Active",
    },
    {
      id: 2,
      admissionNo: "SIMS002",
      name: "Priya Verma",
      class: "9",
      section: "B",
      status: "Active",
    },
  ]);

  // =========================
  // DELETE STUDENT
  // =========================

  const handleDelete = (id) => {

    const confirmDelete = window.confirm(
      "Are you sure you want to delete this student?"
    );

    if (!confirmDelete) return;

    const updatedStudents = students.filter(
      (student) => student.id !== id
    );

    setStudents(updatedStudents);

  };

  // =========================
  // TABLE COLUMNS
  // =========================

  const columns = [
    {
      key: "admissionNo",
      label: "Admission No",
    },
    {
      key: "name",
      label: "Student Name",
    },
    {
      key: "class",
      label: "Class",
    },
    {
      key: "section",
      label: "Section",
    },
    {
      key: "status",
      label: "Status",
    },
    {
      key: "actions",
      label: "Actions",
    },
  ];

  // =========================
  // TABLE DATA
  // =========================

  const tableData = students.map((student) => ({
    ...student,

    actions: (

      <div className="flex gap-2">

        {/* VIEW BUTTON */}
        <button
          onClick={() =>
            navigate(`/dashboard/students/profile/${student.id}`)
          }
          className="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-lg text-sm"
        >
          View
        </button>

        {/* EDIT BUTTON */}
        <button
          onClick={() =>
            navigate(`/dashboard/students/edit/${student.id}`)
          }
          className="bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded-lg text-sm"
        >
          Edit
        </button>

        {/* DELETE BUTTON */}
        <button
          onClick={() =>
            handleDelete(student.id)
          }
          className="bg-red-600 hover:bg-red-700 text-white px-3 py-1 rounded-lg text-sm"
        >
          Delete
        </button>

      </div>

    ),

  }));

  return (

    <div className="space-y-6">

      {/* HEADER */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">

        <div>

          <h1 className="text-3xl font-bold text-gray-800">
            Students Management
          </h1>

          <p className="text-gray-500 mt-1">
            Manage students records
          </p>

        </div>

        <div className="flex gap-3">

          <button
            onClick={() =>
              navigate("/dashboard/students/add")
            }
            className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl font-medium transition"
          >
            Add Student
          </button>

          <ImportButton />

          <ExportButton />

        </div>

      </div>

      {/* SEARCH */}
      <SearchBox placeholder="Search students..." />

      {/* TABLE */}
      <DataTable
        columns={columns}
        data={tableData}
      />

      {/* PAGINATION */}
      <Pagination />

    </div>

  );

};

export default StudentsList;