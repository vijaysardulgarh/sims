// ============================================
// EDIT STREAM
// File: EditStream.jsx
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

import StreamForm from "./StreamForm";

// import streamService from
// "../../../services/academics/streamService";

import streamService from
"./streamService";

const EditStream = () => {

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
  // FETCH STREAM
  // ============================================

  useEffect(() => {

    fetchStream();

  }, []);

  const fetchStream = async () => {

    try {

      const response =
        await streamService.getStream(id);

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load stream"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE STREAM
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await streamService.updateStream(
        id,
        data
      );

      toast.success(
        "Stream updated successfully"
      );

      navigate(
        "/dashboard/academics/streams"
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

        Loading stream...

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
          Edit Stream
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update stream details
        </p>

      </div>

      <StreamForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditStream;