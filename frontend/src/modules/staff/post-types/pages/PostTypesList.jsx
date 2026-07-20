// ============================================
// POST TYPES LIST
// File: PostTypesList.jsx
// ============================================

import {
  useEffect,
  useState,
} from "react";

import {
  useNavigate,
} from "react-router-dom";

import toast from "react-hot-toast";

import DataTable from "@/modules/shared/components/crud/DataTable";
import SearchBox from "@/modules/shared/components/crud/SearchBox";
import Pagination from "@/modules/shared/components/crud/Pagination";
import CrudHeader from "@/modules/shared/components/crud/CrudHeader";
import ActionButtons from "@/modules/shared/components/crud/ActionButtons";
import ConfirmModal from "@/modules/shared/components/dialogs/ConfirmModal";

import postTypeService from "../services/postTypeService";

const PostTypesList = () => {

  // ============================================
  // NAVIGATION
  // ============================================

  const navigate = useNavigate();

  // ============================================
  // STATES
  // ============================================

  const [postTypes, setPostTypes] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [search, setSearch] =
    useState("");

  const [currentPage, setCurrentPage] =
    useState(1);

  const [isModalOpen, setIsModalOpen] =
    useState(false);

  const [selectedId, setSelectedId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH DATA
  // ============================================

  const fetchPostTypes = async () => {

    try {

      setLoading(true);

      const response =
        await postTypeService.getPostTypes();

      const data =
        Array.isArray(response)
          ? response
          : response.results || [];

      setPostTypes(data);

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load post types"
      );

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    fetchPostTypes();

  }, []);

  // ============================================
  // DELETE
  // ============================================

  const handleDelete = async (id) => {

    try {

      await postTypeService.deletePostType(id);

      toast.success(
        "Post Type deleted successfully."
      );

      fetchPostTypes();

    } catch (error) {

      console.error(error);

      toast.error(
        "Delete failed."
      );

    }

  };

  // ============================================
  // FILTER
  // ============================================

  const filteredData =
    postTypes.filter((item) => {

      const keyword =
        search.toLowerCase();

      return (

        item.name
          ?.toLowerCase()
          .includes(keyword)

        ||

        item.description
          ?.toLowerCase()
          .includes(keyword)

      );

    });

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
      key: "name",
      label: "Post Type",
    },

    {
      key: "description",
      label: "Description",
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

      description:
        item.description || "-",

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/staff/post-types/edit/${item.id}`
            )
          }

          onDelete={() => {

            setSelectedId(item.id);

            setIsModalOpen(true);

          }}

        />

      ),

    }));

  // ============================================
  // LOADING
  // ============================================

  if (loading) {

    return (

      <div className="p-6">

        Loading post types...

      </div>

    );

  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Post Types"

        description="Manage staff post types"

        addLabel="Add Post Type"

        onAdd={() =>
          navigate(
            "/dashboard/staff/post-types/add"
          )
        }

      />

      <SearchBox

        placeholder="Search post type..."

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

        title="Delete Post Type"

        message="Are you sure you want to delete this post type?"

        onCancel={() => {

          setSelectedId(null);

          setIsModalOpen(false);

        }}

        onConfirm={() => {

          handleDelete(selectedId);

          setSelectedId(null);

          setIsModalOpen(false);

        }}

      />

    </div>

  );

};

export default PostTypesList;