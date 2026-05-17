// ============================================
// SUBJECTS LIST
// File: SubjectsList.jsx
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
import CrudHeader from "../../../../shared/components/crud/CrudHeader";

import Pagination from "../../../../shared/components/crud/Pagination";
import ActionButtons from "../../../../shared/components/crud/ActionButtons";
import ConfirmModal from "../../../../shared/components/modals/ConfirmModal";

import subjectService from "../services/subjectService";

const SubjectsList = () => {

  const navigate = useNavigate();

  const [subjects, setSubjects] =
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

  const [selectedSubjectId,
    setSelectedSubjectId] =
    useState(null);

  const itemsPerPage = 20;

  const fetchSubjects = async () => {

    try {

      setLoading(true);

      const response =
        await subjectService.getSubjects();

      setSubjects(

        Array.isArray(response)

          ? response

          : response.results || []
      );

    } catch (error) {

      toast.error(
        "Failed to load subjects"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchSubjects();

  }, []);

  const handleDelete = async (id) => {

    try {

      await subjectService.deleteSubject(
        id
      );

      toast.success(
        "Subject deleted successfully"
      );

      fetchSubjects();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  const filteredSubjects =
    subjects.filter((subject) =>

      subject.name
        ?.toLowerCase()
        .includes(
          search.toLowerCase()
        )
    );

  const totalPages =
    Math.ceil(
      filteredSubjects.length /
      itemsPerPage
    );

  const paginatedSubjects =
    filteredSubjects.slice(

      (currentPage - 1) *
      itemsPerPage,

      currentPage *
      itemsPerPage
    );

  const columns = [

    {
      key: "name",
      label: "Subject Name",
    },

    {
      key: "code",
      label: "Code",
    },

    {
      key: "actions",
      label: "Actions",
    },
  ];

  const tableData =
    paginatedSubjects.map((subject) => ({

      ...subject,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/subjects/edit/${subject.id}`
            )
          }

          onDelete={() => {

            setSelectedSubjectId(
              subject.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (
      <div className="p-6">
        Loading subjects...
      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Subjects"

        description="Manage subjects"

        addLabel="Add Subject"

        onAdd={() =>
          navigate(
            "/dashboard/academics/subjects/add"
          )
        }
      />

      <SearchBox

        placeholder="Search subjects..."

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

        title="Delete Subject"

        message="Are you sure you want to delete this subject?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedSubjectId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default SubjectsList;