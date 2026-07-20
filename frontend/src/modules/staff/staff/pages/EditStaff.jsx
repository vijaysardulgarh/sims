// ============================================
// EDIT STAFF
// File: EditStaff.jsx
// ============================================

import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import toast from "react-hot-toast";

import StaffForm from "../components/StaffForm";
import staffService from "../services/staffService";

const EditStaff = () => {

  // ============================================
  // PARAMS
  // ============================================

  const { id } = useParams();

  // ============================================
  // NAVIGATION
  // ============================================

  const navigate = useNavigate();

  // ============================================
  // STATE
  // ============================================

  const [staff, setStaff] = useState(null);

  const [loading, setLoading] = useState(true);

  const [saving, setSaving] = useState(false);

  // ============================================
  // FETCH STAFF
  // ============================================

  useEffect(() => {

    let mounted = true;

    const fetchStaff = async () => {

      try {

        setLoading(true);

        const response =
          await staffService.getStaffMember(id);

        if (mounted) {
          setStaff(response);
        }

      } catch (error) {

        console.error(error);

        toast.error("Failed to load staff.");

      } finally {

        if (mounted) {
          setLoading(false);
        }

      }

    };

    fetchStaff();

    return () => {

      mounted = false;

    };

  }, [id]);

  // ============================================
  // UPDATE STAFF
  // ============================================

  const handleSubmit = async (formData) => {

    try {

      setSaving(true);

      await staffService.updateStaff(
        id,
        formData
      );

      toast.success(
        "Staff updated successfully."
      );

      navigate(
        "/dashboard/staff/staff-profiles"
      );

    } catch (error) {

      console.error(error);

      const errors = error?.response?.data;

      if (
        errors &&
        typeof errors === "object"
      ) {

        Object.entries(errors).forEach(
          ([field, messages]) => {

            toast.error(

              `${field}: ${
                Array.isArray(messages)
                  ? messages.join(", ")
                  : messages
              }`

            );

          }
        );

      } else {

        toast.error(
          "Failed to update staff."
        );

      }

    } finally {

      setSaving(false);

    }

  };

  // ============================================
  // LOADING
  // ============================================

  if (loading) {

    return (

      <div className="flex items-center justify-center h-64">

        <div className="text-center">

          <div className="text-xl font-semibold text-gray-700">
            Loading Staff...
          </div>

          <p className="text-gray-500 mt-2">
            Please wait.
          </p>

        </div>

      </div>

    );

  }

  // ============================================
  // NOT FOUND
  // ============================================

  if (!staff) {

    return (

      <div className="flex items-center justify-center h-64">

        <div className="text-center">

          <h2 className="text-2xl font-bold text-red-600">
            Staff Not Found
          </h2>

          <p className="text-gray-500 mt-2">
            The requested staff record does not exist.
          </p>

          <button
            onClick={() =>
              navigate(
                "/dashboard/staff/staff-profiles"
              )
            }
            className="
              mt-6
              px-6
              py-2
              rounded-lg
              bg-blue-600
              text-white
              hover:bg-blue-700
            "
          >
            Back to Staff List
          </button>

        </div>

      </div>

    );

  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      {/* ============================================
          PAGE HEADER
      ============================================ */}

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Edit Staff
        </h1>

        <p className="
          mt-1
          text-gray-500
        ">
          Update staff information.
        </p>

      </div>

      {/* ============================================
          STAFF FORM
      ============================================ */}

      <StaffForm

        initialData={staff}

        onSubmit={handleSubmit}

        loading={saving}

      />

    </div>

  );

};

export default EditStaff;