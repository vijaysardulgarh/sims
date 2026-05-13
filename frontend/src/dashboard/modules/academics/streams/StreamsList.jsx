// ============================================
// STREAMS LIST
// File: StreamsList.jsx
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

import streamService from
"../../../services/academics/streamService";

const StreamsList = () => {

  const navigate = useNavigate();

  const [streams, setStreams] =
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

  const [selectedStreamId,
    setSelectedStreamId] =
    useState(null);

  const itemsPerPage = 20;

  // ============================================
  // FETCH STREAMS
  // ============================================

  const fetchStreams = async () => {

    try {

      setLoading(true);

      const response =
        await streamService.getStreams();

      const streamsData =

        Array.isArray(response)

          ? response

          : response.results || [];

      setStreams(streamsData);

    } catch (error) {

      toast.error(
        "Failed to load streams"
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchStreams();

  }, []);

  // ============================================
  // DELETE STREAM
  // ============================================

  const handleDelete = async (id) => {

    try {

      await streamService.deleteStream(
        id
      );

      toast.success(
        "Stream deleted successfully"
      );

      fetchStreams();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // ============================================
  // FILTER STREAMS
  // ============================================

  const filteredStreams =
    streams.filter((stream) =>

      stream.name
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
      filteredStreams.length /
      itemsPerPage
    );

  const paginatedStreams =
    filteredStreams.slice(

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
      label: "Stream Name",
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

  // ============================================
  // TABLE DATA
  // ============================================

  const tableData =
    paginatedStreams.map((stream) => ({

      ...stream,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/streams/edit/${stream.id}`
            )
          }

          onDelete={() => {

            setSelectedStreamId(
              stream.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  if (loading) {

    return (

      <div className="p-6">

        Loading streams...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Streams"

        description="Manage school streams"

        addLabel="Add Stream"

        onAdd={() =>
          navigate(
            "/dashboard/academics/streams/add"
          )
        }
      />

      <SearchBox

        placeholder="Search streams..."

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

        title="Delete Stream"

        message="Are you sure you want to delete this stream?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedStreamId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default StreamsList;