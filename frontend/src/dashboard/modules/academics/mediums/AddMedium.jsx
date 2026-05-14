// ============================================
// ADD MEDIUM
// File: AddMedium.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import MediumForm from "./MediumForm";

import mediumService from "./mediumService";


const AddMedium = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE MEDIUM
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await mediumService.createMedium(
        data
      );

      toast.success(
        "Medium created successfully"
      );

      navigate(
        "/dashboard/academics/mediums"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create medium"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="space-y-6">

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Add Medium
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create new medium
        </p>

      </div>

      <MediumForm
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>
  );
};

export default AddMedium;