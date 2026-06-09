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

import associationRoleAssignmentService
from "../services/associationRoleAssignmentService";


const AssociationRoleAssignmentListPage = () => {

  // =========================
  // NAVIGATION
  // =========================

  const navigate = useNavigate();

  // =========================
  // STATE
  // =========================

  const [assignments, setAssignments] =
    useState([]);

  const [loading, setLoading] =
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

  // =========================
  // FETCH
  // =========================

  const fetchAssignments =
    async () => {

      try {

        setLoading(true);

        const response =

          await associationRoleAssignmentService
            .getAssignments();

        const data =

          Array.isArray(response)

            ? response

            : response.results || [];

        setAssignments(
          data
        );

      } catch (error) {

        console.error(
          error
        );

        toast.error(
          "Failed to load assignments"
        );

      } finally {

        setLoading(false);
      }
    };

  useEffect(() => {

    fetchAssignments();

  }, []);

  // =========================
  // DELETE
  // =========================

  const handleDelete =
    async (id) => {

      try {

        await associationRoleAssignmentService
          .deleteAssignment(id);

        toast.success(
          "Assignment deleted successfully"
        );

        fetchAssignments();

      } catch (error) {

        console.error(
          error
        );

        toast.error(
          "Delete failed"
        );
      }
    };

  // =========================
  // PAGINATION
  // =========================

  const totalPages =

    Math.ceil(
      assignments.length /
      itemsPerPage
    );

  const startIndex =

    (
      currentPage - 1
    ) * itemsPerPage;

  const paginatedData =

    assignments.slice(

      startIndex,

      startIndex +
      itemsPerPage
    );

  // =========================
  // COLUMNS
  // =========================

  const columns = [

    {
      key: "association_name",
      label: "Association",
    },

    {
      key: "member_name",
      label: "Member",
    },

    {
      key: "member_type",
      label: "Member Type",
    },

    {
      key: "role_title",
      label: "Role",
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

    paginatedData.map(
      (item) => ({

        ...item,

        actions: (

          <ActionButtons

            onEdit={() =>

              navigate(

                `/dashboard/associations/association-role-assignments/edit/${item.id}`
              )
            }

            onDelete={() => {

              setSelectedId(
                item.id
              );

              setIsModalOpen(
                true
              );

            }}

          />
        ),
      })
    );

  // =========================
  // LOADING
  // =========================

  if (loading) {

    return (

      <div className="p-6">

        Loading assignments...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Association Role Assignments"

        description="Manage association member roles"

        addLabel="Assign Role"

        onAdd={() =>

          navigate(

            "/dashboard/associations/association-role-assignments/add"
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

        title="Delete Assignment"

        message="Are you sure you want to delete this assignment?"

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

export default AssociationRoleAssignmentListPage;