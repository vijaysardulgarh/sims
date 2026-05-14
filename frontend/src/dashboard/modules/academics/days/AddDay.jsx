// ============================================
// ADD DAY
// File: AddDay.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import DayForm from "./DayForm";

// import dayService from
// "../../../services/academics/dayService";


import dayService from "./dayService";

const AddDay = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE DAY
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await dayService.createDay(data);

      toast.success(
        "Day created successfully"
      );

      navigate(
        "/dashboard/academics/days"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create day"
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
          Add Day
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create new day
        </p>

      </div>

      <DayForm
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>
  );
};

export default AddDay;