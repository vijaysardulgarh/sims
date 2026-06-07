// ============================================
// DAYS LIST
// File: DaysList.jsx
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

// import dayService from
// "../../../services/academics/dayService";

import dayService from "../services/dayService";

const DaysList = () => {

  const navigate = useNavigate();

  const [days, setDays] =
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

  const [selectedDayId,
    setSelectedDayId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH DAYS
  // ============================================

  const fetchDays = async () => {

    try {

      setLoading(true);

      const response =
        await dayService.getDays();

      const daysData =

        Array.isArray(response)

          ? response

          : response.results || [];

      const sortedDays = [

        ...daysData

      ].sort((a, b) =>

        a.day_order - b.day_order
      );

      setDays(sortedDays);

    } catch (error) {

      toast.error(
        "Failed to load days"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchDays();

  }, []);

  // ============================================
  // DELETE DAY
  // ============================================

  const handleDelete = async (id) => {

    try {

      await dayService.deleteDay(id);

      toast.success(
        "Day deleted successfully"
      );

      fetchDays();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER DAYS
  // ============================================

  const filteredDays =
    days.filter((day) =>

      day.name
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
      filteredDays.length /
      itemsPerPage
    );

  const paginatedDays =
    filteredDays.slice(

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
      label: "Day Name",
    },

    {
      key: "day_order",
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
    paginatedDays.map((day) => ({

      ...day,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/days/edit/${day.id}`
            )
          }

          onDelete={() => {

            setSelectedDayId(
              day.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading days...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Days"

        description="Manage timetable days"

        addLabel="Add Day"

        onAdd={() =>
          navigate(
            "/dashboard/academics/days/add"
          )
        }
      />

      <SearchBox

        placeholder="Search days..."

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

        title="Delete Day"

        message="Are you sure you want to delete this day?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedDayId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default DaysList;