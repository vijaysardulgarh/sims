// ============================================
// CLASS INCHARGE LIST
// File: ClassInchargeList.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "../../../../dashboard/shared/components/crud/DataTable";
import SearchBox from "../../../../dashboard/shared/components/crud/SearchBox";
import Pagination from "../../../../dashboard/shared/components/crud/Pagination";
import CrudHeader from "../../../../dashboard/shared/components/crud/CrudHeader";
import ActionButtons from "../../../../dashboard/shared/components/crud/ActionButtons";
import ConfirmModal from "../../../../dashboard/shared/components/modals/ConfirmModal";

import classInchargeService from "../services/classInchargeService";

const ClassInchargeList = () => {

  // ============================================
  // NAVIGATION
  // ============================================

  const navigate = useNavigate();

  // ============================================
  // STATES
  // ============================================

  const [classIncharges,
    setClassIncharges] =
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
  // FETCH DATA
  // ============================================

  const fetchClassIncharges =
    async () => {

    try {

      setLoading(true);

      const response =
        await classInchargeService.getClassIncharges();

      const data =

        Array.isArray(response)

          ? response

          : response.results || [];

      setClassIncharges(data);

    } catch (error) {

      toast.error(
        "Failed to load class incharges"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchClassIncharges();

  }, []);

  // ============================================
  // DELETE
  // ============================================

  const handleDelete = async (id) => {

    try {

      await classInchargeService.deleteClassIncharge(
        id
      );

      toast.success(
        "Deleted Successfully"
      );

      fetchClassIncharges();

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
    classIncharges.filter((item) =>

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
      key: "class_name",
      label: "Class",
    },

    {
      key: "section_name",
      label: "Section",
    },

    {
      key: "staff_name",
      label: "Staff",
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
              `/dashboard/staff/class-incharge/edit/${item.id}`
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

        Loading class incharges...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Class Incharge"

        description="Manage class incharge assignments"

        addLabel="Add Incharge"

        onAdd={() =>
          navigate(
            "/dashboard/staff/class-incharge/add"
          )
        }
      />

      <SearchBox

        placeholder="Search class incharge..."

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

        title="Delete Class Incharge"

        message="Are you sure you want to delete this class incharge?"

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

export default ClassInchargeList;