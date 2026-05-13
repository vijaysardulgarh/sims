// ============================================
// CLASSROOMS LIST
// File: ClassroomsList.jsx
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

import classroomService from
"../../../services/academics/classroomService";

const ClassroomsList = () => {

  const navigate = useNavigate();

  const [classrooms,
    setClassrooms] =
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

  const [selectedClassroomId,
    setSelectedClassroomId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH CLASSROOMS
  // ============================================

  const fetchClassrooms = async () => {

    try {

      setLoading(true);

      const response =
        await classroomService.getClassrooms();

      const classroomsData =

        Array.isArray(response)

          ? response

          : response.results || [];

      setClassrooms(classroomsData);

    } catch (error) {

      toast.error(
        "Failed to load classrooms"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchClassrooms();

  }, []);

  // ============================================
  // DELETE CLASSROOM
  // ============================================

  const handleDelete = async (id) => {

    try {

      await classroomService.deleteClassroom(
        id
      );

      toast.success(
        "Classroom deleted successfully"
      );

      fetchClassrooms();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER DATA
  // ============================================

  const filteredClassrooms =
    classrooms.filter((classroom) =>

      classroom.name
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
      filteredClassrooms.length /
      itemsPerPage
    );

  const paginatedClassrooms =
    filteredClassrooms.slice(

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
      label: "Classroom Name",
    },

    {
      key: "room_number",
      label: "Room Number",
    },

    {
      key: "capacity",
      label: "Capacity",
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
    paginatedClassrooms.map((classroom) => ({

      ...classroom,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/classrooms/edit/${classroom.id}`
            )
          }

          onDelete={() => {

            setSelectedClassroomId(
              classroom.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading classrooms...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Classrooms"

        description="Manage classrooms"

        addLabel="Add Classroom"

        onAdd={() =>
          navigate(
            "/dashboard/academics/classrooms/add"
          )
        }
      />

      <SearchBox

        placeholder="Search classrooms..."

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

        title="Delete Classroom"

        message="Are you sure you want to delete this classroom?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedClassroomId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default ClassroomsList;