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

import associationMemberService
from "../services/associationMemberService";

const AssociationMemberListPage = () => {

  const navigate = useNavigate();

  const [members, setMembers] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [currentPage, setCurrentPage] =
    useState(1);

  const [isModalOpen,
    setIsModalOpen] =
    useState(false);

  const [selectedId,
    setSelectedId] =
    useState(null);

  const itemsPerPage = 20;

  const fetchMembers = async () => {

    try {

      setLoading(true);

      const response =
        await associationMemberService.getAll();

      setMembers(
        response.data || response || []
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load members"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchMembers();

  }, []);

  const handleDelete = async (id) => {

    try {

      await associationMemberService.delete(id);

      toast.success(
        "Member deleted successfully"
      );

      fetchMembers();

    } catch (error) {

      console.error(error);

      toast.error(
        "Delete failed"
      );
    }
  };

  const columns = [

    {
      key: "member_name",
      label: "Member Name",
    },

    {
      key: "association_name",
      label: "Association",
    },

    {
      key: "actions",
      label: "Actions",
    },
  ];

  const totalPages = Math.ceil(
    members.length / itemsPerPage
  );

  const paginatedData =
    members.slice(

      (currentPage - 1)
      * itemsPerPage,

      currentPage
      * itemsPerPage
    );

  const tableData =
    paginatedData.map((member) => ({

      ...member,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/associations/association-members/edit/${member.id}`
            )
          }

          onDelete={() => {

            setSelectedId(
              member.id
            );

            setIsModalOpen(
              true
            );
          }}
        />
      ),
    }));

  if (loading) {

    return (
      <div className="p-6">
        Loading...
      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Association Members"

        description="Manage association members"

        addLabel="Add Member"

        onAdd={() =>
          navigate(
            "/dashboard/associations/association-members/add"
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

        onPageChange={setCurrentPage}
      />

      <ConfirmModal

        isOpen={isModalOpen}

        title="Delete Member"

        message="Are you sure?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedId
          );

          setIsModalOpen(false);
        }}
      />

    </div>
  );
};

export default AssociationMemberListPage;