// ============================================
// MEDIUMS LIST
// File: MediumsList.jsx
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

import mediumService from "../services/mediumService";

const MediumsList = () => {

  const navigate = useNavigate();

  const [mediums, setMediums] =
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

  const [selectedMediumId,
    setSelectedMediumId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH MEDIUMS
  // ============================================

  const fetchMediums = async () => {

    try {

      setLoading(true);

      const response =
        await mediumService.getMediums();

      const mediumsData =

        Array.isArray(response)

          ? response

          : response.results || [];

      setMediums(mediumsData);

    } catch (error) {

      toast.error(
        "Failed to load mediums"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchMediums();

  }, []);

  // ============================================
  // DELETE MEDIUM
  // ============================================

  const handleDelete = async (id) => {

    try {

      await mediumService.deleteMedium(
        id
      );

      toast.success(
        "Medium deleted successfully"
      );

      fetchMediums();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER MEDIUMS
  // ============================================

  const filteredMediums =
    mediums.filter((medium) =>

      medium.name
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
      filteredMediums.length /
      itemsPerPage
    );

  const paginatedMediums =
    filteredMediums.slice(

      (currentPage - 1) *
      itemsPerPage,

      currentPage *
      itemsPerPage
    );

  // ============================================
  // TABLE COLUMNS
  // ============================================

  const columns = [

    {
      key: "name",
      label: "Medium Name",
    },

    {
      key: "code",
      label: "Code",
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
    paginatedMediums.map((medium) => ({

      ...medium,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/mediums/edit/${medium.id}`
            )
          }

          onDelete={() => {

            setSelectedMediumId(
              medium.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading mediums...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Mediums"

        description="Manage school mediums"

        addLabel="Add Medium"

        onAdd={() =>
          navigate(
            "/dashboard/academics/mediums/add"
          )
        }
      />

      <SearchBox

        placeholder="Search mediums..."

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

        title="Delete Medium"

        message="Are you sure you want to delete this medium?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedMediumId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default MediumsList;