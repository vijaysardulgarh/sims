// ============================================
// SANCTIONED POSTS LIST
// File: SanctionedPostsList.jsx
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

import sanctionedPostService
from "./sanctionedPostService";

const SanctionedPostsList = () => {

  const navigate = useNavigate();

  const [posts, setPosts] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [search, setSearch] =
    useState("");

  const [currentPage,
    setCurrentPage] =
    useState(1);

  const [selectedId,
    setSelectedId] =
    useState(null);

  const [isModalOpen,
    setIsModalOpen] =
    useState(false);

  const itemsPerPage = 20;

  // ============================================
  // FETCH
  // ============================================

  const fetchPosts = async () => {

    try {

      setLoading(true);

      const response =
        await sanctionedPostService.getSanctionedPosts();

      const data =

        Array.isArray(response)

          ? response

          : response.results || [];

      setPosts(data);

    } catch (error) {

      toast.error(
        "Failed to load data"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchPosts();

  }, []);

  // ============================================
  // DELETE
  // ============================================

  const handleDelete = async (id) => {

    try {

      await sanctionedPostService.deleteSanctionedPost(
        id
      );

      toast.success(
        "Deleted Successfully"
      );

      fetchPosts();

    } catch (error) {

      toast.error(
        "Delete Failed"
      );
    }
  };

  // ============================================
  // FILTER
  // ============================================

  const filteredData =
    posts.filter((item) =>

      item.post_type_name
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
  // COLUMNS
  // ============================================

  const columns = [

    {
      key: "post_type_name",
      label: "Post Type",
    },

    {
      key: "sanctioned_count",
      label: "Sanctioned",
    },

    {
      key: "filled_count",
      label: "Filled",
    },

    {
      key: "remarks",
      label: "Remarks",
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

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/staff/sanctioned-posts/edit/${item.id}`
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

        Loading sanctioned posts...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Sanctioned Posts"

        description="Manage sanctioned staff posts"

        addLabel="Add Post"

        onAdd={() =>
          navigate(
            "/dashboard/staff/sanctioned-posts/add"
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

        title="Delete Post"

        message="Are you sure you want to delete this post?"

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

export default SanctionedPostsList;