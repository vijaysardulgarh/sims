import {
  useEffect,
  useState
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import AssociationMeetingForm
from "../components/AssociationMeetingForm";

import associationMeetingService
from "../services/associationMeetingService";


const EditAssociationMeeting = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const [initialData,
    setInitialData] =
    useState({});

  // =========================
  // FETCH MEETING
  // =========================

  useEffect(() => {

    fetchMeeting();

  }, [id]);

  const fetchMeeting = async () => {

    try {

      setLoading(true);

      const response =

        await associationMeetingService
          .getById(id);

      setInitialData(
        response
      );

    } catch (error) {

      console.error(
        error
      );

      toast.error(
        "Failed to load meeting"
      );

    } finally {

      setLoading(false);
    }
  };

  // =========================
  // UPDATE MEETING
  // =========================

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await associationMeetingService.update(
        id,
        data
      );

      toast.success(
        "Meeting updated successfully"
      );

      navigate(
        "/dashboard/associations/association-meetings"
      );

    } catch (error) {

      console.error(
        error
      );

      console.log(
        error.response?.data
      );

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

  return (

    <div className="space-y-6">

      <h1
        className="
          text-2xl
          font-bold
        "
      >

        Edit Association Meeting

      </h1>

      <AssociationMeetingForm

        initialData={
          initialData
        }

        onSubmit={
          handleSubmit
        }

        loading={
          loading
        }

      />

    </div>
  );
};

export default EditAssociationMeeting;