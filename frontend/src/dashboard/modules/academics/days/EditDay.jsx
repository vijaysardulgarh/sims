// ============================================
// EDIT DAY
// File: EditDay.jsx
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

import DayForm from "./DayForm";

import dayService from
"../../../services/academics/dayService";

const EditDay = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const [pageLoading,
    setPageLoading] =
    useState(true);

  const [initialData,
    setInitialData] =
    useState({});

  // ============================================
  // FETCH DAY
  // ============================================

  useEffect(() => {

    fetchDay();

  }, []);

  const fetchDay = async () => {

    try {

      const response =
        await dayService.getDay(id);

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load day"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE DAY
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await dayService.updateDay(
        id,
        data
      );

      toast.success(
        "Day updated successfully"
      );

      navigate(
        "/dashboard/academics/days"
      );

    } catch (error) {

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Update failed"
      );

    } finally {

      setLoading(false);
    }
  };

  if (pageLoading) {

    return (

      <div className="p-6">

        Loading day...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Edit Day
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update day details
        </p>

      </div>

      <DayForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditDay;