// ============================================
// TEACHER ATTENDANCE LIST
// File: TeacherAttendanceList.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "@/modules/shared/components/crud/DataTable";
import SearchBox from "@/modules/shared/components/crud/SearchBox";
import Pagination from "@/modules/shared/components/crud/Pagination";
import CrudHeader from "@/modules/shared/components/crud/CrudHeader";
import ActionButtons from "@/modules/shared/components/crud/ActionButtons";
import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";

import teacherAttendanceService from "../services/teacherAttendanceService";

const TeacherAttendanceList = () => {

  const navigate = useNavigate();

  const [attendance, setAttendance] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [search, setSearch] =
    useState("");

  const [currentPage,
    setCurrentPage] =
    useState(1);

  const [selectedId,
    setSelectedId] =
    useState(null);

  const [isModalOpen,
    setIsModalOpen] =
    useState(false);

  const itemsPerPage = 20;

  // ============================================
  // FETCH
  // ============================================

  const fetchAttendance =
    async () => {

    try {

      setLoading(true);

      const response =
        await teacherAttendanceService.getTeacherAttendance();

      const data =

        Array.isArray(response)

          ? response

          : response.results || [];

      setAttendance(data);

    } catch (error) {

      toast.error(
        "Failed to load attendance"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchAttendance();

  }, []);

  // ============================================
  // DELETE
  // ============================================

  const handleDelete = async (id) => {

    try {

      await teacherAttendanceService.deleteTeacherAttendance(
        id
      );

      toast.success(
        "Deleted Successfully"
      );

      fetchAttendance();

    } catch (error) {

      toast.error(
        "Delete Failed"
      );
    }
  };

  // ============================================
  // FILTER
  // ============================================

  const filteredData =
    attendance.filter((item) =>

      item.staff_name
        ?.toLowerCase()
        .includes(
          search.toLowerCase()
        )
    );

  // ============================================
  // PAGINATION
  // ============================================

  const totalPages =
    Math.ceil(
      filteredData.length /
      itemsPerPage
    );

  const paginatedData =
    filteredData.slice(

      (currentPage - 1) *
      itemsPerPage,

      currentPage *
      itemsPerPage
    );

  // ============================================
  // COLUMNS
  // ============================================

  const columns = [

    {
      key: "staff_name",
      label: "Staff",
    },

    {
      key: "attendance_date",
      label: "Date",
    },

    {
      key: "status",
      label: "Status",
    },

    {
      key: "remarks",
      label: "Remarks",
    },

    {
      key: "actions",
      label: "Actions",
    },
  ];

  // ============================================
  // TABLE DATA
  // ============================================

  const tableData =
    paginatedData.map((item) => ({

      ...item,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/staff/teacher-attendance/edit/${item.id}`
            )
          }

          onDelete={() => {

            setSelectedId(item.id);

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading attendance...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Teacher Attendance"

        description="Manage teacher attendance"

        addLabel="Add Attendance"

        onAdd={() =>
          navigate(
            "/dashboard/staff/teacher-attendance/add"
          )
        }
      />

      <SearchBox

        placeholder="Search teacher..."

        value={search}

        onChange={(e) =>
          setSearch(e.target.value)
        }
      />

      <DataTable
        columns={columns}
        data={tableData}
      />

      <Pagination

        currentPage={currentPage}

        totalPages={totalPages}

        onPageChange={setCurrentPage}
      />

      <ConfirmModal

        isOpen={isModalOpen}

        title="Delete Attendance"

        message="Are you sure you want to delete this attendance record?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(selectedId);

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default TeacherAttendanceList;