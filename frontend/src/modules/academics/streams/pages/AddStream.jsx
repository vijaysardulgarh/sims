// ============================================
// ADD STREAM
// File: AddStream.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import StreamForm from "../components/StreamForm";

// import streamService from
// "../../../services/academics/streamService";

import streamService from "../services/streamService";



const AddStream = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE STREAM
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await streamService.createStream(
        data
      );

      toast.success(
        "Stream created successfully"
      );

      navigate(
        "/dashboard/academics/streams"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create stream"
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
          Add Stream
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create new stream
        </p>

      </div>

      <StreamForm
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>
  );
};

export default AddStream;