// ============================================
// CLASS SUBJECTS LIST
// File: ClassSubjectsList.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "../../../../shared/components/crud/DataTable";

import SearchBox from "../../../../shared/components/crud/SearchBox";

import Pagination from "../../../../shared/components/crud/Pagination";

import CrudHeader from "../../../../shared/components/crud/CrudHeader";

import ActionButtons from "../../../../shared/components/crud/ActionButtons";

import ConfirmModal from "../../../../shared/components/modals/ConfirmModal";

import classSubjectService from "../services/classSubjectService";

const ClassSubjectsList = () => {

  const navigate = useNavigate();

  const [classSubjects,
    setClassSubjects] =
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

  const [selectedId,
    setSelectedId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH CLASS SUBJECTS
  // ============================================

  const fetchClassSubjects = async () => {

    try {

      setLoading(true);

      const response =
        await classSubjectService.getClassSubjects();

      const data =

        Array.isArray(response)

          ? response

          : response.results || [];

      setClassSubjects(data);

    } catch (error) {

      toast.error(
        "Failed to load class subjects"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchClassSubjects();

  }, []);

  // ============================================
  // DELETE
  // ============================================

  const handleDelete = async (id) => {

    try {

      await classSubjectService.deleteClassSubject(
        id
      );

      toast.success(
        "Class subject deleted successfully"
      );

      fetchClassSubjects();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER
  // ============================================

  const filteredData =
    classSubjects.filter((item) =>

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
      filteredData.length /
      itemsPerPage
    );

  const paginatedData =
    filteredData.slice(

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
      key: "subject_name",
      label: "Subject",
    },

    {
      key: "stream_name",
      label: "Stream",
    },

    {
      key: "is_optional",
      label: "Optional",
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
    paginatedData.map((item) => ({

      ...item,

      is_optional:

        item.is_optional

          ? "Yes"

          : "No",

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/class-subjects/edit/${item.id}`
            )
          }

          onDelete={() => {

            setSelectedId(item.id);

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading class subjects...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Class Subjects"

        description="Manage class subject assignments"

        addLabel="Add Class Subject"

        onAdd={() =>
          navigate(
            "/dashboard/academics/class-subjects/add"
          )
        }
      />

      <SearchBox

        placeholder="Search class subjects..."

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

        title="Delete Class Subject"

        message="Are you sure you want to delete this class subject?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(selectedId);

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default ClassSubjectsList;