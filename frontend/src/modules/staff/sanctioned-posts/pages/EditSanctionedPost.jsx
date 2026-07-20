// ============================================
// EDIT SANCTIONED POST
// File: EditSanctionedPost.jsx
// ============================================

import {
  useEffect,
  useState,
} from "react";

import {
  useNavigate,
  useParams,
} from "react-router-dom";

import toast from "react-hot-toast";

import SanctionedPostForm
  from "../components/SanctionedPostForm";

import sanctionedPostService
  from "../services/sanctionedPostService";

const EditSanctionedPost = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(true);

  const [initialData,
    setInitialData] =
    useState({});

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchData();

  }, []);

  const fetchData = async () => {

    try {

      setLoading(true);

      const response =
        await sanctionedPostService.getSanctionedPost(
          id
        );

      setInitialData(response);

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load sanctioned post."
      );

    } finally {

      setLoading(false);

    }

  };

  // ============================================
  // UPDATE
  // ============================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await sanctionedPostService.updateSanctionedPost(

        id,

        formData

      );

      toast.success(
        "Sanctioned Post Updated Successfully"
      );

      navigate(
        "/dashboard/staff/sanctioned-posts"
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to update sanctioned post."
      );

    } finally {

      setLoading(false);

    }

  };

  if (
    loading &&
    !initialData.id
  ) {

    return (

      <div className="p-10">

        Loading...

      </div>

    );

  }

  return (

    <div className="space-y-6">

      <h1
        className="
          text-3xl
          font-bold
          text-gray-800
        "
      >

        Edit Sanctioned Post

      </h1>

      <SanctionedPostForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>

  );

};

export default EditSanctionedPost;