// ============================================
// SECTIONS LIST
// File: SectionsList.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "../../../../dashboard/shared/components/crud/DataTable";
import SearchBox from "../../../../dashboard/shared/components/crud/SearchBox";
import Pagination from "../../../../dashboard/shared/components/crud/Pagination";
import CrudHeader from "../../../../dashboard/shared/components/crud/CrudHeader";
import ActionButtons from "../../../../dashboard/shared/components/crud/ActionButtons";
import ConfirmModal from "../../../../dashboard/shared/components/modals/ConfirmModal";

import sectionService from "../services/sectionService";


const SectionsList = () => {

  const navigate = useNavigate();

  const [sections, setSections] =
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

  const [selectedSectionId,
    setSelectedSectionId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH SECTIONS
  // ============================================

  const fetchSections = async () => {

    try {

      setLoading(true);

      const response =
        await sectionService.getSections();

      const sectionsData =

        Array.isArray(response)

          ? response

          : response.results || [];

      setSections(
        sectionsData
      );

    } catch (error) {

      console.error(
        error
      );

      toast.error(
        "Failed to load sections"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchSections();

  }, []);

  // ============================================
  // DELETE SECTION
  // ============================================

  const handleDelete = async (
    id
  ) => {

    try {

      await sectionService.deleteSection(
        id
      );

      toast.success(
        "Section deleted successfully"
      );

      fetchSections();

    } catch (error) {

      console.error(
        error
      );

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER SECTIONS
  // ============================================

  const filteredSections =
    sections.filter((section) => {

      const searchText =
        search.toLowerCase();

      return (

        section.name
          ?.toLowerCase()
          .includes(searchText)

        ||

        section.class_name
          ?.toLowerCase()
          .includes(searchText)

        ||

        section.medium_name
          ?.toLowerCase()
          .includes(searchText)

        ||

        section.stream_name
          ?.toLowerCase()
          .includes(searchText)

        ||

        section.classroom_name
          ?.toLowerCase()
          .includes(searchText)
      );
    });

  // ============================================
  // PAGINATION
  // ============================================

  const totalPages =
    Math.ceil(

      filteredSections.length /

      itemsPerPage
    );

  const paginatedSections =
    filteredSections.slice(

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
      key: "name",
      label: "Section",
    },

    {
      key: "medium_name",
      label: "Medium",
    },

    {
      key: "stream_name",
      label: "Stream",
    },

    {
      key: "sub_stream",
      label: "Sub Stream",
    },

    {
      key: "classroom_name",
      label: "Classroom",
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
    paginatedSections.map(
      (section) => ({

        ...section,

        class_name:
          section.class_name || "-",

        medium_name:
          section.medium_name || "-",

        stream_name:
          section.stream_name || "-",

        sub_stream:
          section.sub_stream || "-",

        classroom_name:
          section.classroom_name || "-",

        actions: (

          <ActionButtons

            onEdit={() =>
              navigate(
                `/dashboard/academics/sections/edit/${section.id}`
              )
            }

            onDelete={() => {

              setSelectedSectionId(
                section.id
              );

              setIsModalOpen(
                true
              );
            }}
          />
        ),
      })
    );

  // ============================================
  // LOADING
  // ============================================

  if (loading) {

    return (

      <div className="p-6">

        Loading sections...

      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Sections"

        description="Manage class sections"

        addLabel="Add Section"

        onAdd={() =>
          navigate(
            "/dashboard/academics/sections/add"
          )
        }
      />

      <SearchBox

        placeholder="Search sections..."

        value={search}

        onChange={(e) =>
          setSearch(
            e.target.value
          )
        }
      />

      <DataTable

        columns={columns}

        data={tableData}
      />

      <Pagination

        currentPage={
          currentPage
        }

        totalPages={
          totalPages
        }

        onPageChange={
          setCurrentPage
        }
      />

      <ConfirmModal

        isOpen={
          isModalOpen
        }

        title="Delete Section"

        message="Are you sure you want to delete this section?"

        onCancel={() =>
          setIsModalOpen(
            false
          )
        }

        onConfirm={() => {

          handleDelete(
            selectedSectionId
          );

          setIsModalOpen(
            false
          );
        }}
      />

    </div>
  );
};

export default SectionsList;