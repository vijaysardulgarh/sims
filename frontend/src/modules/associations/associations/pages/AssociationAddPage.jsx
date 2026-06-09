import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import AssociationForm from "../components/AssociationForm";

import associationService from "../services/associationService";


const AssociationAddPage = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // =========================
  // CREATE ASSOCIATION
  // =========================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await associationService.createAssociation(
        data
      );

      toast.success(
        "Association created successfully"
      );

      navigate(
        "/dashboard/associations/associations"
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

          : "Failed to create association"
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

        Add Association

      </h1>

      <AssociationForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default AssociationAddPage;