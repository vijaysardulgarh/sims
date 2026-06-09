import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast
from "react-hot-toast";

import AssociationRoleAssignmentForm
from "../components/AssociationRoleAssignmentForm";

import associationRoleAssignmentService
from "../services/associationRoleAssignmentService";


const AddAssociationRoleAssignment = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // =========================
  // CREATE ASSIGNMENT
  // =========================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await associationRoleAssignmentService
        .createAssignment(data);

      toast.success(
        "Role assigned successfully"
      );

      navigate(
        "/dashboard/associations/association-role-assignments"
      );

    } catch (error) {

      console.error(error);

      console.log(
        error.response?.data
      );

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to assign role"
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

        Assign Role

      </h1>

      <AssociationRoleAssignmentForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default AddAssociationRoleAssignment;