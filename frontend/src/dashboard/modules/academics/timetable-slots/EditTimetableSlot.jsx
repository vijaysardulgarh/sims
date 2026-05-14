// ============================================
// EDIT TIMETABLE SLOT
// File: EditTimetableSlot.jsx
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

import TimetableSlotForm from "./TimetableSlotForm";

// import timetableSlotService from
// "../../../services/academics/timetableSlotService";

import timetableSlotService from "./timetableSlotService";

const EditTimetableSlot = () => {

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
  // FETCH SLOT
  // ============================================

  useEffect(() => {

    fetchSlot();

  }, []);

  const fetchSlot = async () => {

    try {

      const response =
        await timetableSlotService.getTimetableSlot(
          id
        );

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load slot"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE SLOT
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await timetableSlotService.updateTimetableSlot(
        id,
        data
      );

      toast.success(
        "Timetable slot updated successfully"
      );

      navigate(
        "/dashboard/academics/timetable-slots"
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

        Loading timetable slot...

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
          Edit Timetable Slot
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update timetable slot details
        </p>

      </div>

      <TimetableSlotForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditTimetableSlot;