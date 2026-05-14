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

// import sectionService from
// "../../../services/academics/sectionService";

import sectionService from "./sectionService";

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

      setSections(sectionsData);

    } catch (error) {

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

  const handleDelete = async (id) => {

    try {

      await sectionService.deleteSection(
        id
      );

      toast.success(
        "Section deleted successfully"
      );

      fetchSections();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER SECTIONS
  // ============================================

  const filteredSections =
    sections.filter((section) =>

      section.name
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
      key: "name",
      label: "Section Name",
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
    paginatedSections.map((section) => ({

      ...section,

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

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading sections...

      </div>
    );
  }

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

        title="Delete Section"

        message="Are you sure you want to delete this section?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedSectionId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default SectionsList;