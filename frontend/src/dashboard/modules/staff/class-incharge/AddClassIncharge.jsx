// ============================================
// ADD CLASS INCHARGE
// File: AddClassIncharge.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import ClassInchargeForm
from "./ClassInchargeForm";

import classInchargeService
from "./classInchargeService";

const AddClassIncharge = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE
  // ============================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await classInchargeService.createClassIncharge(

        formData

      );

      toast.success(
        "Class Incharge Added Successfully"
      );

      navigate(
        "/dashboard/staff/class-incharge"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to add class incharge"
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

          Add Class Incharge

        </h1>

        <p className="
          text-gray-500
          mt-1
        ">

          Assign teacher as class incharge

        </p>

      </div>

      <ClassInchargeForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default AddClassIncharge;