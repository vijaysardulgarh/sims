// ============================================
// TIMETABLE SLOTS LIST
// File: TimetableSlotsList.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from
"../../../components/crud/DataTable";

import SearchBox from
"../../../components/crud/SearchBox";

import Pagination from
"../../../components/crud/Pagination";

import CrudHeader from
"../../../components/crud/CrudHeader";

import ActionButtons from
"../../../components/crud/ActionButtons";

import ConfirmModal from
"../../../components/modals/ConfirmModal";

// import timetableSlotService from
// "../../../services/academics/timetableSlotService";

import timetableSlotService from "./timetableSlotService";

const TimetableSlotsList = () => {

  const navigate = useNavigate();

  const [slots, setSlots] =
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

  const [selectedSlotId,
    setSelectedSlotId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH SLOTS
  // ============================================

  const fetchSlots = async () => {

    try {

      setLoading(true);

      const response =
        await timetableSlotService.getTimetableSlots();

      const slotData =

        Array.isArray(response)

          ? response

          : response.results || [];

      const sortedSlots = [

        ...slotData

      ].sort((a, b) =>

        a.slot_order - b.slot_order
      );

      setSlots(sortedSlots);

    } catch (error) {

      toast.error(
        "Failed to load timetable slots"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchSlots();

  }, []);

  // ============================================
  // DELETE SLOT
  // ============================================

  const handleDelete = async (id) => {

    try {

      await timetableSlotService.deleteTimetableSlot(
        id
      );

      toast.success(
        "Timetable slot deleted successfully"
      );

      fetchSlots();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER DATA
  // ============================================

  const filteredSlots =
    slots.filter((slot) =>

      slot.name
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
      filteredSlots.length /
      itemsPerPage
    );

  const paginatedSlots =
    filteredSlots.slice(

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
      label: "Slot Name",
    },

    {
      key: "start_time",
      label: "Start Time",
    },

    {
      key: "end_time",
      label: "End Time",
    },

    {
      key: "slot_order",
      label: "Order",
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
    paginatedSlots.map((slot) => ({

      ...slot,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/timetable-slots/edit/${slot.id}`
            )
          }

          onDelete={() => {

            setSelectedSlotId(
              slot.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading timetable slots...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Timetable Slots"

        description="Manage timetable periods"

        addLabel="Add Slot"

        onAdd={() =>
          navigate(
            "/dashboard/academics/timetable-slots/add"
          )
        }
      />

      <SearchBox

        placeholder="Search timetable slots..."

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

        title="Delete Timetable Slot"

        message="Are you sure you want to delete this timetable slot?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedSlotId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default TimetableSlotsList;