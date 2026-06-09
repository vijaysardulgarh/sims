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

import associationMeetingService from "../services/associationMeetingService";


const AssociationMeetingListPage = () => {

  // =========================
  // NAVIGATION
  // =========================

  const navigate = useNavigate();

  // =========================
  // STATE
  // =========================

  const [meetings, setMeetings] =
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
  // FETCH MEETINGS
  // =========================

  const fetchMeetings = async () => {

    try {

      setLoading(true);

      const response =
        await associationMeetingService.getAll();

      const meetingsData =

        Array.isArray(response)

          ? response

          : response?.data?.data ||

            response?.data ||

            response?.results ||

            [];

      setMeetings(
        meetingsData
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load meetings"
      );

      setMeetings([]);

    } finally {

      setLoading(false);
    }
  };

  // =========================
  // LOAD DATA
  // =========================

  useEffect(() => {

    fetchMeetings();

  }, []);

  // =========================
  // DELETE MEETING
  // =========================

  const handleDelete = async (id) => {

    try {

      await associationMeetingService.delete(
        id
      );

      toast.success(
        "Meeting deleted successfully"
      );

      fetchMeetings();

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

  const totalPages =

    Math.ceil(
      meetings.length /
      itemsPerPage
    );

  const startIndex =

    (
      currentPage - 1
    ) * itemsPerPage;

  const paginatedMeetings =

    meetings.slice(

      startIndex,

      startIndex +
      itemsPerPage
    );

  // =========================
  // TABLE COLUMNS
  // =========================

  const columns = [

    {
      key: "association_name",
      label: "Association",
    },

    {
      key: "meeting_date",
      label: "Meeting Date",
    },

    {
      key: "location",
      label: "Location",
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

    paginatedMeetings.map(
      (meeting) => ({

        ...meeting,

        actions: (

          <ActionButtons

            onEdit={() =>
              navigate(
                `/dashboard/associations/association-meetings/edit/${meeting.id}`
              )
            }

            onDelete={() => {

              setSelectedId(
                meeting.id
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

        Loading meetings...

      </div>
    );
  }

  // =========================
  // PAGE
  // =========================

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Association Meetings"

        description="Manage association meetings"

        addLabel="Add Meeting"

        onAdd={() =>
          navigate(
            "/dashboard/associations/association-meetings/add"
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

        title="Delete Meeting"

        message="Are you sure you want to delete this meeting?"

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

export default AssociationMeetingListPage;