// ============================================
// ADD TIMETABLE
// File: AddTimetable.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

// import TimetableForm from "./TimetableForm";

// import timetableService from
// "../../../services/academics/timetableService";

import TimetableForm from
"./TimetableForm";

import timetableService from "./timetableService";

const AddTimetable = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE TIMETABLE
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await timetableService.createTimetable(
        data
      );

      toast.success(
        "Timetable created successfully"
      );

      navigate(
        "/dashboard/academics/timetable"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create timetable"
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
          Add Timetable
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create timetable entry
        </p>

      </div>

      <TimetableForm

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default AddTimetable;