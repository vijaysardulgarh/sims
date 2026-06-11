// ============================================
// TIMETABLE LIST
// File: TimetableList.jsx
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
"../../../shared/components/crud/DataTable";

import SearchBox from
"../../../shared/components/crud/SearchBox";

import Pagination from
"../../../shared/components/crud/Pagination";

import CrudHeader from
"../../../shared/components/crud/CrudHeader";

import ActionButtons from
"../../../shared/components/crud/ActionButtons";

import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";

// import timetableService from
// "../../../services/academics/timetableService";

import timetableService from "../services/timetableService";

const TimetableList = () => {

  const navigate = useNavigate();

  const [timetables,
    setTimetables] =
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

  const [selectedTimetableId,
    setSelectedTimetableId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH TIMETABLES
  // ============================================

  const fetchTimetables = async () => {

    try {

      setLoading(true);

      const response =
        await timetableService.getTimetables();

      const timetableData =

        Array.isArray(response)

          ? response

          : response.results || [];

      setTimetables(timetableData);

    } catch (error) {

      toast.error(
        "Failed to load timetable"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchTimetables();

  }, []);

  // ============================================
  // DELETE TIMETABLE
  // ============================================

  const handleDelete = async (id) => {

    try {

      await timetableService.deleteTimetable(
        id
      );

      toast.success(
        "Timetable deleted successfully"
      );

      fetchTimetables();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER DATA
  // ============================================

  const filteredTimetables =
    timetables.filter((item) =>

      item.subject_name
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
      filteredTimetables.length /
      itemsPerPage
    );

  const paginatedTimetables =
    filteredTimetables.slice(

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
      key: "class_name",
      label: "Class",
    },

    {
      key: "section_name",
      label: "Section",
    },

    {
      key: "subject_name",
      label: "Subject",
    },

    {
      key: "teacher_name",
      label: "Teacher",
    },

    {
      key: "day_name",
      label: "Day",
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
      key: "actions",
      label: "Actions",
    },
  ];

  // ============================================
  // TABLE DATA
  // ============================================

  const tableData =
    paginatedTimetables.map((item) => ({

      ...item,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/timetable/edit/${item.id}`
            )
          }

          onDelete={() => {

            setSelectedTimetableId(
              item.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading timetable...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Timetable"

        description="Manage school timetable"

        addLabel="Add Timetable"

        onAdd={() =>
          navigate(
            "/dashboard/academics/timetable/add"
          )
        }
      />

      <SearchBox

        placeholder="Search timetable..."

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

        title="Delete Timetable"

        message="Are you sure you want to delete this timetable entry?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedTimetableId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default TimetableList;