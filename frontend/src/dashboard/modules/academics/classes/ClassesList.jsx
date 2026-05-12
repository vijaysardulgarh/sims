import {
  useEffect,
  useState
} from "react";

import { useNavigate }
from "react-router-dom";

import toast
from "react-hot-toast";

import DataTable
from "../../../components/crud/DataTable";

import SearchBox
from "../../../components/crud/SearchBox";

import Pagination
from "../../../components/crud/Pagination";

import CrudHeader
from "../../../components/crud/CrudHeader";

import ActionButtons
from "../../../components/crud/ActionButtons";

import ConfirmModal
from "../../../components/modals/ConfirmModal";

import classService
from "../../../services/academics/classService";


const ClassesList = () => {

  // =========================
  // NAVIGATION
  // =========================

  const navigate = useNavigate();

  // =========================
  // STATE
  // =========================

  const [classes, setClasses] =
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

  const [selectedClassId,
    setSelectedClassId] =
    useState(null);

  const itemsPerPage = 20;

  // =========================
  // FETCH CLASSES
  // =========================

  const fetchClasses = async () => {

    try {

      setLoading(true);

      const response =
        await classService.getClasses();

      const classesData =

        Array.isArray(response)

          ? response

          : response.results || [];

      setClasses(classesData);

    } catch (error) {

      toast.error(
        "Failed to load classes"
      );

    } finally {

      setLoading(false);
    }
  };

  // =========================
  // LOAD DATA
  // =========================

  useEffect(() => {

    fetchClasses();

  }, []);

  // =========================
  // DELETE CLASS
  // =========================

  const handleDelete = async (id) => {

    try {

      await classService.deleteClass(id);

      toast.success(
        "Class deleted successfully"
      );

      fetchClasses();

    } catch (error) {

      toast.error(
        "Delete failed"
      );
    }
  };

  // =========================
  // FILTER DATA
  // =========================

  const filteredClasses =
    classes.filter((cls) =>

      cls.name
        ?.toLowerCase()
        .includes(
          search.toLowerCase()
        )
    );

  // =========================
  // PAGINATION
  // =========================

  const totalPages =
    Math.ceil(
      filteredClasses.length /
      itemsPerPage
    );

  const startIndex =
    (currentPage - 1) *
    itemsPerPage;

  const paginatedClasses =
    filteredClasses.slice(
      startIndex,
      startIndex + itemsPerPage
    );

  // =========================
  // TABLE COLUMNS
  // =========================

  const columns = [

    {
      key: "name",
      label: "Class Name",
    },

    {
      key: "class_order",
      label: "Order",
    },

    {
      key: "actions",
      label: "Actions",
    },
  ];

  // =========================
  // TABLE DATA
  // =========================

  const tableData =
    paginatedClasses.map((cls) => ({

      ...cls,

      actions: (

        <ActionButtons

          onEdit={() =>
            navigate(
              `/dashboard/academics/classes/edit/${cls.id}`
            )
          }

          onDelete={() => {

            setSelectedClassId(
              cls.id
            );

            setIsModalOpen(true);
          }}
        />
      ),
    }));

  // =========================
  // LOADING
  // =========================

  if (loading) {

    return (

      <div className="p-6">

        Loading classes...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <CrudHeader

        title="Classes"

        description="Manage school classes"

        addLabel="Add Class"

        onAdd={() =>
          navigate(
            "/dashboard/academics/classes/add"
          )
        }
      />

      <SearchBox

        placeholder="Search classes..."

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

        title="Delete Class"

        message="Are you sure you want to delete this class?"

        onCancel={() =>
          setIsModalOpen(false)
        }

        onConfirm={() => {

          handleDelete(
            selectedClassId
          );

          setIsModalOpen(false);

        }}
      />

    </div>
  );
};

export default ClassesList;