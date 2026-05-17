// ============================================
// EDIT STAFF
// File: EditStaff.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import StaffForm from "./StaffForm";

import staffService from "./staffService";

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
  // STATES
  // ============================================

  const [staff, setStaff] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH STAFF
  // ============================================

  useEffect(() => {

    fetchStaff();

  }, []);

  const fetchStaff = async () => {

    try {

      const response =
        await staffService.getStaffMember(
          id
        );

      setStaff(response);

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to load staff"
      );

    } finally {

      setLoading(false);
    }
  };

  // ============================================
  // UPDATE STAFF
  // ============================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await staffService.updateStaff(

        id,

        formData

      );

      toast.success(
        "Staff Updated Successfully"
      );

      navigate(
        "/dashboard/staff/staff"
      );

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to update staff"
      );

    } finally {

      setLoading(false);
    }
  };

  // ============================================
  // LOADING
  // ============================================

  if (loading && !staff) {

    return (

      <div className="p-10">

        <h1 className="
          text-2xl
          font-bold
        ">

          Loading...

        </h1>

      </div>
    );
  }

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

          Edit Staff

        </h1>

        <p className="
          text-gray-500
          mt-1
        ">

          Update staff details

        </p>

      </div>

      <StaffForm

        initialData={staff}

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default EditStaff;