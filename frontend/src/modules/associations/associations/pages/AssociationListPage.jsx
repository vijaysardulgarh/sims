// ============================================
// IMPORTS
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
import Pagination from "@/modules/shared/components/crud/Pagination";
import CrudHeader from "@/modules/shared/components/crud/CrudHeader";
import ActionButtons from "@/modules/shared/components/crud/ActionButtons";

import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";

import associationService from "../services/associationService";


// ============================================
// COMPONENT
// ============================================

const AssociationListPage = () => {

  const navigate = useNavigate();

  // ==========================================
  // STATE
  // ==========================================

  const [associations,
    setAssociations] =
    useState([]);

  const [loading,
    setLoading] =
    useState(true);

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

  // ==========================================
  // FETCH ASSOCIATIONS
  // ==========================================

  const fetchAssociations = async () => {

    try {

      setLoading(true);

      const response =
        await associationService.getAssociations();

      console.log(
        "Association Response:",
        response
      );

      let associationsData = [];

      if (
        Array.isArray(response)
      ) {

        associationsData =
          response;

      } else if (
        Array.isArray(
          response?.data
        )
      ) {

        associationsData =
          response.data;

      }

      setAssociations(
        associationsData
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load associations"
      );

      setAssociations([]);

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchAssociations();

  }, []);

  // ==========================================
  // DELETE
  // ==========================================

  const handleDelete = async (id) => {

    try {

      await associationService.deleteAssociation(
        id
      );

      toast.success(
        "Association deleted successfully"
      );

      fetchAssociations();

    } catch (error) {

      console.error(error);

      toast.error(
        "Delete failed"
      );
    }
  };

  // ==========================================
  // PAGINATION
  // ==========================================

  const totalPages = Math.ceil(

    associations.length /

    itemsPerPage
  );

  const startIndex =

    (currentPage - 1) *

    itemsPerPage;

  const paginatedAssociations =

    associations.slice(

      startIndex,

      startIndex + itemsPerPage
    );

  // ==========================================
  // TABLE COLUMNS
  // ==========================================

  const columns = [

    {
      key: "name",
      label: "Association Name",
    },

    {
      key: "association_type_display",
      label: "Type",
    },

    {
      key: "status_display",
      label: "Status",
    },

    {
      key: "priority",
      label: "Priority",
    },

    {
      key: "actions",
      label: "Actions",
    },
  ];

  // ==========================================
  // TABLE DATA
  // ==========================================

  const tableData =

    paginatedAssociations.map(
      (association) => ({

        ...association,

        actions: (

          <ActionButtons

            onEdit={() =>
              navigate(
                `/dashboard/associations/associations/edit/${association.id}`
              )
            }

            onDelete={() => {

              setSelectedId(
                association.id
              );

              setIsModalOpen(
                true
              );
            }}

          />
        ),
      })
    );

  // ==========================================
  // LOADING
  // ==========================================

  if (loading) {

    return (

      <div className="p-6">

        Loading associations...

      </div>
    );
  }

  // ==========================================
  // UI
  // ==========================================

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Associations"

        description="Manage school associations"

        addLabel="Add Association"

        onAdd={() =>
          navigate(
            "/dashboard/associations/associations/add"
          )
        }
      />

      <DataTable

        columns={columns}

        data={tableData}

        currentPage={currentPage}

        itemsPerPage={itemsPerPage}
      />

      <Pagination

        currentPage={currentPage}

        totalPages={totalPages}

        onPageChange={
          setCurrentPage
        }
      />

      <ConfirmModal

        isOpen={
          isModalOpen
        }

        title="Delete Association"

        message="Are you sure you want to delete this association?"

        onCancel={() =>
          setIsModalOpen(
            false
          )
        }

        onConfirm={() => {

          handleDelete(
            selectedId
          );

          setIsModalOpen(
            false
          );
        }}
      />

    </div>
  );
};

export default AssociationListPage;