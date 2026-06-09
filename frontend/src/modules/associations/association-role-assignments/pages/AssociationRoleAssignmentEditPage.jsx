import {
  useEffect,
  useState
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import AssociationRoleAssignmentForm
from "../components/AssociationRoleAssignmentForm";

import associationRoleAssignmentService
from "../services/associationRoleAssignmentService";


const EditAssociationRoleAssignment = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const [initialData,
    setInitialData] =
    useState({});

  // =========================
  // FETCH ASSIGNMENT
  // =========================

  useEffect(() => {

    fetchAssignment();

  }, [id]);

  const fetchAssignment = async () => {

    try {

      setLoading(true);

      const response =

        await associationRoleAssignmentService
          .getAssignment(id);

      setInitialData(
        response
      );

    } catch (error) {

      console.error(
        error
      );

      toast.error(
        "Failed to load assignment"
      );

    } finally {

      setLoading(false);
    }
  };

  // =========================
  // UPDATE ASSIGNMENT
  // =========================

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await associationRoleAssignmentService
        .updateAssignment(
          id,
          data
        );

      toast.success(
        "Assignment updated successfully"
      );

      navigate(
        "/dashboard/associations/association-role-assignments"
      );

    } catch (error) {

      console.error(
        error
      );

      console.log(
        error.response?.data
      );

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Update failed"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="space-y-6">

      <h1
        className="
          text-2xl
          font-bold
        "
      >

        Edit Role Assignment

      </h1>

      <AssociationRoleAssignmentForm

        initialData={
          initialData
        }

        onSubmit={
          handleSubmit
        }

        loading={
          loading
        }

      />

    </div>
  );
};

export default EditAssociationRoleAssignment;