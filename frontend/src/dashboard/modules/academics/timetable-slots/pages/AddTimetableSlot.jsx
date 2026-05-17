// ============================================
// ADD TIMETABLE SLOT
// File: AddTimetableSlot.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import TimetableSlotForm from "../components/TimetableSlotForm";

// import timetableSlotService from
// "../../../services/academics/timetableSlotService";

import timetableSlotService from "../services/timetableSlotService";

const AddTimetableSlot = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE SLOT
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await timetableSlotService.createTimetableSlot(
        data
      );

      toast.success(
        "Timetable slot created successfully"
      );

      navigate(
        "/dashboard/academics/timetable-slots"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create slot"
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
          Add Timetable Slot
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create new timetable slot
        </p>

      </div>

      <TimetableSlotForm

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default AddTimetableSlot;