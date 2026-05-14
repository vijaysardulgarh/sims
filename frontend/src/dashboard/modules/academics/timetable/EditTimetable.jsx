// ============================================
// EDIT TIMETABLE
// File: EditTimetable.jsx
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

import TimetableForm from "./TimetableForm";

// import timetableService from
// "../../../services/academics/timetableService";

import timetableService from "./timetableService";

const EditTimetable = () => {

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
  // FETCH TIMETABLE
  // ============================================

  useEffect(() => {

    fetchTimetable();

  }, []);

  const fetchTimetable = async () => {

    try {

      const response =
        await timetableService.getTimetable(id);

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load timetable"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE TIMETABLE
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await timetableService.updateTimetable(
        id,
        data
      );

      toast.success(
        "Timetable updated successfully"
      );

      navigate(
        "/dashboard/academics/timetable"
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

        Loading timetable...

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
          Edit Timetable
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update timetable entry
        </p>

      </div>

      <TimetableForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditTimetable;