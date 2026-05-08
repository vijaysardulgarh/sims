import { useState } from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "../../components/crud/DataTable";
import SearchBox from "../../components/crud/SearchBox";
import Pagination from "../../components/crud/Pagination";
import ImportButton from "../../components/crud/ImportButton";
import ExportButton from "../../components/crud/ExportButton";

import ConfirmModal from "../../components/modals/ConfirmModal";

import ActionButtons from "../../components/crud/ActionButtons";
import CrudHeader from "../../components/crud/CrudHeader";
import StatusToggle from "../../components/crud/StatusToggle";
import TableFilters from "../../components/crud/TableFilters";
import BulkActions from "../../components/crud/BulkActions";

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
  // SEARCH STATE
  // =========================

  const [search, setSearch] =
    useState("");

  // =========================
  // TABLE FILTER STATES
  // =========================

  const [classFilter, setClassFilter] =
    useState("");

  const [statusFilter, setStatusFilter] =
    useState("");

  // =========================
  // PAGINATION
  // =========================

  const [currentPage, setCurrentPage] =
    useState(1);

  const itemsPerPage = 5;

  // =========================
  // CONFIRMATION MODAL
  // =========================

  const [isModalOpen, setIsModalOpen] =
    useState(false);

  const [selectedStudentId,
    setSelectedStudentId] =
    useState(null);

  // =========================
  // BULK SELECTION
  // =========================

  const [selectedStudents,
    setSelectedStudents] =
    useState([]);

  // =========================
  // STRONG CONFIRMATION
  // =========================

  const [confirmText,
    setConfirmText] =
    useState("");

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

    const updatedStudents =
      students.filter(
        (student) =>
          student.id !== id
      );

    setStudents(updatedStudents);

    localStorage.setItem(
      "students",
      JSON.stringify(updatedStudents)
    );

    toast.success(
      "Student Deleted Successfully"
    );

  };

  // =========================
  // BULK DELETE
  // =========================

  const handleBulkDelete = () => {

    // =========================
    // NO SELECTION
    // =========================

    if (
      selectedStudents.length === 0
    ) {

      toast.error(
        "No Students Selected"
      );

      return;

    }

    // =========================
    // STRONG CONFIRMATION
    // =========================

    if (
      selectedStudents.length > 20
    ) {

      const userInput =
        window.prompt(

          `You are about to delete ${selectedStudents.length} students.

Type DELETE to continue.`

        );

      if (userInput !== "DELETE") {

        toast.error(
          "Bulk Delete Cancelled"
        );

        return;

      }

    }

    // =========================
    // DELETE STUDENTS
    // =========================

    const updatedStudents =
      students.filter(
        (student) =>
          !selectedStudents.includes(
            student.id
          )
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
    // RESET SELECTION
    // =========================

    setSelectedStudents([]);

    // =========================
    // SUCCESS MESSAGE
    // =========================

    toast.success(
      `${selectedStudents.length} Students Deleted`
    );

  };

  // =========================
  // SELECT ALL RECORDS
  // =========================

  const handleSelectAllRecords = () => {

    const allStudentIds =
      filteredStudents.map(
        (student) => student.id
      );

    setSelectedStudents(
      allStudentIds
    );

    toast.success(
      `${allStudentIds.length} Records Selected`
    );

  };

  // =========================
  // TOGGLE STATUS
  // =========================

  const handleStatusToggle = (id) => {

    const updatedStudents =
      students.map((student) => {

        if (student.id === id) {

          return {

            ...student,

            status:
              student.status === "Active"
                ? "Inactive"
                : "Active",

          };

        }

        return student;

      });

    setStudents(updatedStudents);

    localStorage.setItem(
      "students",
      JSON.stringify(updatedStudents)
    );

    toast.success(
      "Status Updated Successfully"
    );

  };

  // =========================
  // FILTER STUDENTS
  // =========================

  const filteredStudents =
    students.filter((student) => {

      const searchValue =
        search.toLowerCase();

      return (

        (
          student.name
            .toLowerCase()
            .includes(searchValue)

          ||

          student.admissionNo
            .toLowerCase()
            .includes(searchValue)

          ||

          student.class
            .toLowerCase()
            .includes(searchValue)
        )

        &&

        (
          classFilter === "" ||
          student.class === classFilter
        )

        &&

        (
          statusFilter === "" ||
          student.status === statusFilter
        )

      );

    });

  // =========================
  // PAGINATION LOGIC
  // =========================

  const totalPages =
    Math.ceil(
      filteredStudents.length /
      itemsPerPage
    );

  const startIndex =
    (currentPage - 1) *
    itemsPerPage;

  const endIndex =
    startIndex + itemsPerPage;

  const paginatedStudents =
    filteredStudents.slice(
      startIndex,
      endIndex
    );

  // =========================
  // TABLE COLUMNS
  // =========================

  const columns = [

    {
      key: "select",

      label: (

        <input
          type="checkbox"

          checked={
            paginatedStudents.length > 0 &&

            paginatedStudents.every(
              (student) =>
                selectedStudents.includes(
                  student.id
                )
            )
          }

          onChange={(e) => {

            if (e.target.checked) {

              const pageStudentIds =
                paginatedStudents.map(
                  (student) => student.id
                );

              setSelectedStudents([
                ...new Set([
                  ...selectedStudents,
                  ...pageStudentIds,
                ]),
              ]);

            } else {

              const pageStudentIds =
                paginatedStudents.map(
                  (student) => student.id
                );

              setSelectedStudents(

                selectedStudents.filter(
                  (id) =>
                    !pageStudentIds.includes(id)
                )

              );

            }

          }}
        />

      ),
    },

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
    paginatedStudents.map((student) => ({

      ...student,

      select: (

        <input
          type="checkbox"
          checked={selectedStudents.includes(student.id)}
          onChange={(e) => {

            if (e.target.checked) {

              setSelectedStudents([
                ...selectedStudents,
                student.id,
              ]);

            } else {

              setSelectedStudents(
                selectedStudents.filter(
                  (id) => id !== student.id
                )
              );

            }

          }}
        />

      ),

      status: (

        <StatusToggle

          status={student.status}

          onToggle={() =>
            handleStatusToggle(student.id)
          }

        />

      ),

      actions: (

        <ActionButtons

          onView={() =>
            navigate(
              `/dashboard/students/profile/${student.id}`
            )
          }

          onEdit={() =>
            navigate(
              `/dashboard/students/edit/${student.id}`
            )
          }

          onDelete={() => {

            setSelectedStudentId(
              student.id
            );

            setIsModalOpen(true);

          }}

        />

      ),

    }));

  return (

    <div className="space-y-6">

      {/* HEADER */}
      <CrudHeader
        title="Students Management"
        description="Manage students records"
        addLabel="Add Student"
        onAdd={() =>
          navigate("/dashboard/students/add")
        }
      >

        <ImportButton />

        <ExportButton />

      </CrudHeader>

      {/* BULK ACTIONS */}
      <BulkActions
        selectedCount={
          selectedStudents.length
        }
        onDelete={handleBulkDelete}
        onSelectAll={
          handleSelectAllRecords
        }
      />

      {/* SEARCH */}
      <SearchBox
        placeholder="Search students..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />

      {/* TABLE FILTERS */}
      <TableFilters
        classFilter={classFilter}
        setClassFilter={setClassFilter}
        statusFilter={statusFilter}
        setStatusFilter={setStatusFilter}
      />

      {/* TABLE */}
      <DataTable
        columns={columns}
        data={tableData}
      />

      {/* PAGINATION */}
      <Pagination
        currentPage={currentPage}
        totalPages={totalPages}
        onPageChange={setCurrentPage}
      />

      {/* CONFIRM MODAL */}
      <ConfirmModal
        isOpen={isModalOpen}
        title="Delete Student"
        message="Are you sure you want to delete this student?"
        onCancel={() =>
          setIsModalOpen(false)
        }
        onConfirm={() => {

          handleDelete(
            selectedStudentId
          );

          setIsModalOpen(false);

        }}
      />

    </div>

  );

};

export default StudentsList;