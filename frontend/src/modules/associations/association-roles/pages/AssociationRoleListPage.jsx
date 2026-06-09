import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import CrudHeader from "@/modules/shared/components/crud/CrudHeader";
import DataTable from "@/modules/shared/components/crud/DataTable";
import Pagination from "@/modules/shared/components/crud/Pagination";
import ActionButtons from "@/modules/shared/components/crud/ActionButtons";
import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";

import associationRoleService from "../services/associationRoleService";

const AssociationRoleListPage = () => {

  const navigate = useNavigate();

  const [roles, setRoles] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [currentPage, setCurrentPage] =
    useState(1);

  const [selectedId, setSelectedId] =
    useState(null);

  const [isModalOpen, setIsModalOpen] =
    useState(false);

  const itemsPerPage = 20;

  // =========================
  // FETCH ROLES
  // =========================

  const fetchRoles = async () => {

    try {

      setLoading(true);

      const response =
        await associationRoleService.getAll();

      const rolesData =

        response?.data ||

        response?.results ||

        response ||

        [];

      setRoles(
        Array.isArray(rolesData)
          ? rolesData
          : []
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load roles"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchRoles();

  }, []);

  // =========================
  // DELETE
  // =========================

  const handleDelete = async (id) => {

    try {

      await associationRoleService.delete(
        id
      );

      toast.success(
        "Role deleted successfully"
      );

      fetchRoles();

    } catch (error) {

      console.error(error);

      toast.error(
        "Delete failed"
      );
    }
  };

  // =========================
  // PAGINATION
  // =========================

  const totalPages = Math.ceil(
    roles.length / itemsPerPage
  );

  const startIndex =
    (currentPage - 1) *
    itemsPerPage;

  const paginatedRoles =
    roles.slice(
      startIndex,
      startIndex + itemsPerPage
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
      key: "title",
      label: "Role Title",
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
    paginatedRoles.map(
      (role) => ({

        ...role,

        actions: (

          <ActionButtons

            onEdit={() =>
              navigate(
                `/dashboard/associations/association-roles/edit/${role.id}`
              )
            }

            onDelete={() => {

              setSelectedId(
                role.id
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

        Loading roles...

      </div>

    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Association Roles"

        description="Manage association roles"

        addLabel="Add Role"

        onAdd={() =>
          navigate(
            "/dashboard/associations/association-roles/add"
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

        title="Delete Role"

        message="Are you sure you want to delete this role?"

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

export default AssociationRoleListPage;