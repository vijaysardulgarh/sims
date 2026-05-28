// ============================================
// STAFF LIST
// File: StaffList.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "../../../../shared/components/crud/DataTable";
import SearchBox from "../../../../shared/components/crud/SearchBox";
import Pagination from "../../../../shared/components/crud/Pagination";
import CrudHeader from "../../../../shared/components/crud/CrudHeader";
import ActionButtons from "../../../../shared/components/crud/ActionButtons";
import ConfirmModal from "../../../../shared/components/modals/ConfirmModal";

import staffService from "../services/staffService";


const StaffList = () => {

  // ============================================
  // NAVIGATION
  // ============================================

  const navigate = useNavigate();

  // ============================================
  // STATES
  // ============================================

  const [staff, setStaff] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [search, setSearch] =
    useState("");

  const [currentPage,
    setCurrentPage] =
    useState(1);

  const [isModalOpen,
    setIsModalOpen] =
    useState(false);

  const [selectedId,
    setSelectedId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH STAFF
  // ============================================

  const fetchStaff = async () => {

    try {

      setLoading(true);

      const response =
        await staffService.getStaff();

      const data =

        Array.isArray(response)

          ? response

          : response.results || [];

      setStaff(data);

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load staff"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchStaff();

  }, []);

  // ============================================
  // DELETE
  // ============================================

  const handleDelete = async (id) => {

    try {

      await staffService.deleteStaff(
        id
      );

      toast.success(
        "Deleted Successfully"
      );

      fetchStaff();

    } catch (error) {

      console.error(error);

      toast.error(
        "Delete Failed"
      );
    }
  };

  // ============================================
  // FILTER
  // ============================================

  const filteredData =
    staff.filter((item) =>

      (item.name || "")

        .toLowerCase()

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
      key: "employee_id",
      label: "Employee ID",
    },

    {
      key: "full_name",
      label: "Name",
    },

    {
      key: "email",
      label: "Email",
    },

    {
      key: "mobile_number",
      label: "Mobile",
    },

    {
      key: "post_type_name",
      label: "Post Type",
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

      full_name:
        item.name,

      actions: (

        <ActionButtons

          onView={() =>
            navigate(
              `/dashboard/staff/staff-profiles/profile/${item.id}`
            )
          }

          onEdit={() =>
            navigate(
              `/dashboard/staff/staff-profiles/edit/${item.id}`
            )
          }

          onDelete={() => {

            setSelectedId(item.id);

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  // ============================================
  // LOADING
  // ============================================

  if (loading) {

    return (

      <div className="p-6">

        Loading staff...

      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Staff"

        description="Manage school staff"

        addLabel="Add Staff"

        onAdd={() =>
          navigate(
            "/dashboard/staff/staff-profiles/add"
          )
        }
      />

      <SearchBox

        placeholder="Search staff..."

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

        title="Delete Staff"

        message="Are you sure you want to delete this staff?"

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

export default StaffList;