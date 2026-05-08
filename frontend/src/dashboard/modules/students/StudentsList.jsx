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
  // DEFAULT STUDENTS
  // =========================

  const defaultStudents = [

    {
      id: 1,
      admissionNo: "SIMS001",
      name: "Rahul Sharma",
      class: "10",
      section: "A",
      phone: "9876543210",
      status: "Active",
    },

    {
      id: 2,
      admissionNo: "SIMS002",
      name: "Priya Verma",
      class: "9",
      section: "B",
      phone: "9876543211",
      status: "Active",
    },

  ];

  // =========================
  // LOAD FROM STORAGE
  // =========================

  const savedStudents =
    JSON.parse(
      localStorage.getItem("students")
    );

  // =========================
  // STUDENTS STATE
  // =========================

  const [students, setStudents] =
    useState(
      savedStudents || defaultStudents
    );

  // =========================
  // SAVE TO STORAGE
  // =========================

  localStorage.setItem(
    "students",
    JSON.stringify(students)
  );

  // =========================
  // DELETE STUDENT
  // =========================

  const handleDelete = (id) => {

    const confirmDelete =
      window.confirm(
        "Are you sure you want to delete this student?"
      );

    if (!confirmDelete) return;

    // =========================
    // REMOVE STUDENT
    // =========================

    const updatedStudents =
      students.filter(
        (student) =>
          student.id !== id
      );

    // =========================
    // UPDATE STATE
    // =========================

    setStudents(updatedStudents);

    // =========================
    // UPDATE STORAGE
    // =========================

    localStorage.setItem(
      "students",
      JSON.stringify(updatedStudents)
    );

    // =========================
    // SUCCESS MESSAGE
    // =========================

    alert(
      "Student Deleted Successfully"
    );

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

  const tableData =
    students.map((student) => ({

      ...student,

      actions: (

        <div className="flex gap-2">

          {/* VIEW BUTTON */}
          <button
            onClick={() =>
              navigate(
                `/dashboard/students/profile/${student.id}`
              )
            }
            className="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-lg text-sm"
          >
            View
          </button>

          {/* EDIT BUTTON */}
          <button
            onClick={() =>
              navigate(
                `/dashboard/students/edit/${student.id}`
              )
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

          {/* ADD STUDENT */}
          <button
            onClick={() =>
              navigate(
                "/dashboard/students/add"
              )
            }
            className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl font-medium transition"
          >
            Add Student
          </button>

          {/* IMPORT */}
          <ImportButton />

          {/* EXPORT */}
          <ExportButton />

        </div>

      </div>

      {/* SEARCH */}
      <SearchBox
        placeholder="Search students..."
      />

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