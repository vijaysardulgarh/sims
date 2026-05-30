// ============================================
// ADD STAFF
// File: AddStaff.jsx
// ============================================

import { useState } from "react";
import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import StaffForm from "../components/StaffForm";
import staffService from "../services/staffService";

const AddStaff = () => {

  // ============================================
  // NAVIGATION
  // ============================================

  const navigate = useNavigate();

  // ============================================
  // STATE
  // ============================================

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // SUBMIT
  // ============================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await staffService.createStaff(
        formData
      );

      toast.success(
        "Staff added successfully"
      );

      navigate(
        "/dashboard/staff/staff-profiles"
      );

    } catch (error) {

      console.error(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to add staff"
      );

    } finally {

      setLoading(false);
    }
  };

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Add Staff
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create a new staff record
        </p>

      </div>

      <StaffForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default AddStaff;