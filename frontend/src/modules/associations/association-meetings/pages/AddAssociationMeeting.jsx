import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast
from "react-hot-toast";

import AssociationMeetingForm
from "../components/AssociationMeetingForm";

import associationMeetingService
from "../services/associationMeetingService";


const AddAssociationMeeting = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // =========================
  // CREATE MEETING
  // =========================

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await associationMeetingService.create(
        data
      );

      toast.success(
        "Meeting created successfully"
      );

      navigate(
        "/dashboard/associations/association-meetings/"
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

          : "Failed to create meeting"
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

        Add Association Meeting

      </h1>

      <AssociationMeetingForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default AddAssociationMeeting;