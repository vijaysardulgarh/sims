import {
  useState,
  useEffect
} from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "../../../../dashboard/shared/components/crud/DataTable";
import SearchBox from "../../../../dashboard/shared/components/crud/SearchBox";
import Pagination from "../../../../dashboard/shared/components/crud/Pagination";
import ImportButton from "../../../../dashboard/shared/components/crud/ImportButton";
import ExportButton from "../../../../dashboard/shared/components/crud/ExportButton";

import ConfirmModal from "../../../../dashboard/shared/components/modals/ConfirmModal";

import ActionButtons from "../../../../dashboard/shared/components/crud/ActionButtons";
import CrudHeader from "../../../../dashboard/shared/components/crud/CrudHeader";
import StatusToggle from "../../../../dashboard/shared/components/crud/StatusToggle";
import TableFilters from "../../../../dashboard/shared/components/crud/TableFilters";
import BulkActions from "../../../../dashboard/shared/components/crud/BulkActions";

import studentService from "../services/studentService";


const StudentsList = () => {

  // =========================
  // NAVIGATION
  // =========================

  const navigate = useNavigate();

  // =========================
  // STUDENTS STATE
  // =========================

  const [students, setStudents] =
    useState([]);

  // =========================
  // LOADING STATE
  // =========================

  const [loading, setLoading] =
    useState(true);

  // =========================
  // SEARCH STATE
  // =========================

  const [search, setSearch] =
    useState("");

  // =========================
  // FILTER STATES
  // =========================

  const [classFilter, setClassFilter] =
    useState("");

  const [sectionFilter, setSectionFilter] =
    useState("");

  const [genderFilter, setGenderFilter] =
  useState("");
  
  const [categoryFilter, setCategoryFilter] =
    useState("");  

  const [statusFilter, setStatusFilter] =
    useState("");

  // =========================
  // PAGINATION
  // =========================

  const [currentPage, setCurrentPage] =
    useState(1);

  const itemsPerPage = 40;

  // =========================
  // CONFIRM MODAL
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
  // IMPORT EXPORT
  // =========================

  const [file, setFile] =
    useState(null);

  const [importLoading,
    setImportLoading] =
    useState(false);

  // =========================
  // FETCH STUDENTS
  // =========================

  const fetchStudents = async () => {

    try {

      setLoading(true);

      const response =
        await studentService.getStudents();

      const studentsData =

        Array.isArray(response)

          ? response

          : response.results || [];

      // =========================
      // FORMAT STUDENTS
      // =========================

      const formattedStudents =
        studentsData.map((student) => ({

          id:

            student.srn ||

            student.id,

          admissionNo:
            student.admission_number || "",

          name:
            student.full_name_aadhar || "",

          class:

            student.student_class_data?.name ||

            student.student_class?.name ||

            student.class_name ||

            "",

          gender:
            student.gender || "",
      
          category:
            student.category || "",  

          section:

            student.section_data?.name ||

            student.section?.name ||

            student.section_name ||

            "",

          phone:
            student.father_mobile || "",

          status:

            student.is_active
              ? "Active"
              : "Inactive",
        }));

      setStudents(
        formattedStudents
      );

    } catch (error) {

      console.error(
        "FETCH ERROR:",
        error
      );

      toast.error(
        "Failed to load students"
      );

    } finally {

      setLoading(false);
    }
  };

  // =========================
  // LOAD STUDENTS
  // =========================

  useEffect(() => {

    fetchStudents();

  }, []);

  // =========================
  // FILE CHANGE
  // =========================

  const handleFileChange = (e) => {

    setFile(
      e.target.files[0]
    );
  };

  // =========================
  // IMPORT STUDENTS
  // =========================

  const handleImport = async () => {

    if (!file) {

      toast.error(
        "Please select Excel file"
      );

      return;
    }

    try {

      setImportLoading(true);

      const response =
        await studentService.importStudents(
          file
        );

      if (response?.success) {

        toast.success(

          response.message ||

          "Students Imported Successfully"
        );

        fetchStudents();

      } else {

        toast.error(

          response?.error ||

          "Import Failed"
        );
      }

    } catch (error) {

      toast.error(

        error?.response?.data?.error ||

        error?.message ||

        "Import Failed"
      );

    } finally {

      setImportLoading(false);
    }
  };

  // =========================
  // EXPORT STUDENTS
  // =========================

  const handleExport = () => {

    studentService.exportStudents();

    toast.success(
      "Export Started"
    );
  };

  // =========================
  // DELETE STUDENT
  // =========================

  const handleDelete = async (id) => {

    try {

      await studentService.deleteStudent(id);

      toast.success(
        "Student Deleted Successfully"
      );

      fetchStudents();

    } catch (error) {

      toast.error(
        "Delete Failed"
      );
    }
  };

  // =========================
  // BULK DELETE
  // =========================

  const handleBulkDelete = async () => {

    // =====================================
    // NO RECORD SELECTED
    // =====================================
  
    if (
      selectedStudents.length === 0
    ) {
  
      toast.error(
        "No students selected"
      );
  
      return;
    }
  
    // =====================================
    // CONFIRM DELETE
    // =====================================
  
    const confirmDelete =
      window.confirm(
  
        `Are you sure you want to delete ${selectedStudents.length} students?`
      );
  
    if (!confirmDelete) {
  
      return;
    }
  
    try {
  
      // =====================================
      // DELETE ALL SELECTED
      // =====================================
  
      await Promise.all(
  
        selectedStudents.map((id) =>
  
          studentService.deleteStudent(id)
        )
      );
  
      // =====================================
      // SUCCESS
      // =====================================
  
      toast.success(
  
        `${selectedStudents.length} students deleted successfully`
      );
  
      // =====================================
      // CLEAR SELECTION
      // =====================================
  
      setSelectedStudents([]);
  
      // =====================================
      // REFRESH LIST
      // =====================================
  
      fetchStudents();
  
    } catch (error) {
  
      console.error(
        "BULK DELETE ERROR:",
        error
      );
  
      toast.error(
        "Failed to delete selected students"
      );
    }
  };

  // =========================
  // SELECT ALL
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

  const handleStatusToggle = async (id) => {

    try {

      const currentStudent =
        students.find(
          (student) => student.id === id
        );

      if (!currentStudent) {

        toast.error(
          "Student not found"
        );

        return;
      }

      const updatedStatus =

        currentStudent.status === "Active"

          ? false

          : true;

      await studentService.updateStudent(

        id,

        {
          is_active: updatedStatus
        }
      );

      fetchStudents();

      toast.success(
        "Status Updated Successfully"
      );

    } catch (error) {

      console.error(
        "STATUS UPDATE ERROR:",
        error
      );

      toast.error(
        "Failed to update status"
      );
    }
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

          ||

          student.section
            .toLowerCase()
            .includes(searchValue)

          ||

          student.gender
            .toLowerCase()
            .includes(searchValue)
          
          ||
          
          student.category
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
          sectionFilter === "" ||

          student.section === sectionFilter
        )

        &&

        (
          genderFilter === "" ||

          student.gender === genderFilter
        )

        &&

        (
          categoryFilter === "" ||

          student.category === categoryFilter
        )
        
        &&

        (
          statusFilter === "" ||

          student.status === statusFilter
        )
      );

    });

  // =========================
  // PAGINATION
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

  // =========================
  // LOADING UI
  // =========================

  if (loading) {

    return (

      <div className="p-6">

        Loading students...

      </div>
    );
  }

  return (

    <div className="space-y-6 p-6">

      {/* STATS */}

      <div className="
        grid
        grid-cols-1
        md:grid-cols-4
        gap-4
      ">

        <div className="
          bg-white
          rounded-xl
          shadow
          p-5
        ">
          <p className="text-gray-500 text-sm">
            Total Students
          </p>

          <h2 className="
            text-3xl
            font-bold
            mt-2
          ">
            {students.length}
          </h2>
        </div>

        <div className="
          bg-white
          rounded-xl
          shadow
          p-5
        ">
          <p className="text-gray-500 text-sm">
            Active Students
          </p>

          <h2 className="
            text-3xl
            font-bold
            mt-2
          ">
            {
              students.filter(
                s => s.status === "Active"
              ).length
            }
          </h2>
        </div>

        <div className="
          bg-white
          rounded-xl
          shadow
          p-5
        ">
          <p className="text-gray-500 text-sm">
            Male Students
          </p>

          <h2 className="
            text-3xl
            font-bold
            mt-2
          ">
            {
              students.filter(
                s => s.gender === "Male"
              ).length
            }
          </h2>
        </div>

        <div className="
          bg-white
          rounded-xl
          shadow
          p-5
        ">
          <p className="text-gray-500 text-sm">
            Female Students
          </p>

          <h2 className="
            text-3xl
            font-bold
            mt-2
          ">
            {
              students.filter(
                s => s.gender === "Female"
              ).length
            }
          </h2>
        </div>

      </div>

      {/* HEADER */}

      <CrudHeader
        title="Students"
        description="
          Manage student records,
          admissions and profiles
        "
        addLabel="+ New Student"
        onAdd={() =>
          navigate(
            "/dashboard/students/list/add"
          )
        }
      >

        <div className="
          flex
          items-center
          gap-3
        ">

          <input
            type="file"
            accept=".xlsx,.xls"
            onChange={handleFileChange}
            className="
              border
              rounded-lg
              px-3
              py-2
            "
          />

          <ImportButton
            onClick={handleImport}
            disabled={importLoading}
          />

          <ExportButton
            onClick={handleExport}
          />

        </div>

      </CrudHeader>

      {/* SEARCH */}

      <SearchBox
        placeholder="
          Search student,
          admission no,
          class,
          section,
          phone...
        "
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />

      {/* FILTERS */}

      <TableFilters

        classFilter={classFilter}
        setClassFilter={setClassFilter}

        sectionFilter={sectionFilter}
        setSectionFilter={setSectionFilter}

        genderFilter={genderFilter}
        setGenderFilter={setGenderFilter}

        categoryFilter={categoryFilter}
        setCategoryFilter={setCategoryFilter}

        statusFilter={statusFilter}
        setStatusFilter={setStatusFilter}

        students={students}

      />

      {/* BULK ACTIONS */}

      {selectedStudents.length > 0 && (

        <BulkActions

          selectedCount={
            selectedStudents.length
          }

          onDelete={
            handleBulkDelete
          }

          onSelectAll={
            handleSelectAllRecords
          }

        />

      )}

      {/* RECORD COUNT */}

      <div className="
        flex
        justify-between
        text-sm
        text-gray-500
      ">

        <span>

          Showing

          {" "}

          {startIndex + 1}

          -

          {Math.min(
            endIndex,
            filteredStudents.length
          )}

          of

          {" "}

          {filteredStudents.length}

          students

        </span>

      </div>

      {/* TABLE */}

      <DataTable
        columns={columns}
        data={tableData}
      />

      {/* PAGINATION */}

      <Pagination

        currentPage={
          currentPage
        }

        totalPages={
          totalPages
        }

        onPageChange={
          setCurrentPage
        }

      />

      {/* DELETE MODAL */}

      <ConfirmModal

        isOpen={isModalOpen}

        title="Delete Student"

        message="
          Are you sure you want
          to delete this student?
        "

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