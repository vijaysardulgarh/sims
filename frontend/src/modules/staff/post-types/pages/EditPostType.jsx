// ============================================
// EDIT POST TYPE
// File: EditPostType.jsx
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

import PostTypeForm from "../components/PostTypeForm";
import postTypeService from "../services/postTypeService";

const EditPostType = () => {

  // ============================================
  // PARAMS
  // ============================================

  const { id } = useParams();

  // ============================================
  // NAVIGATION
  // ============================================

  const navigate = useNavigate();

  // ============================================
  // STATES
  // ============================================

  const [loading, setLoading] =
    useState(true);

  const [initialData, setInitialData] =
    useState({});

  // ============================================
  // FETCH POST TYPE
  // ============================================

  useEffect(() => {

    fetchPostType();

  }, [id]);

  const fetchPostType = async () => {

    try {

      setLoading(true);

      const response =
        await postTypeService.getPostType(id);

      setInitialData(response);

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load post type."
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

      await postTypeService.updatePostType(

        id,

        formData

      );

      toast.success(
        "Post Type updated successfully."
      );

      navigate(
        "/dashboard/staff/post-types"
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to update post type."
      );

    } finally {

      setLoading(false);

    }

  };

  // ============================================
  // LOADING
  // ============================================

  if (loading && !initialData.id) {

    return (

      <div className="p-10">

        Loading...

      </div>

    );

  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      <div>

        <h1
          className="
            text-3xl
            font-bold
            text-gray-800
          "
        >

          Edit Post Type

        </h1>

        <p
          className="
            text-gray-500
            mt-1
          "
        >

          Update post type details

        </p>

      </div>

      <PostTypeForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>

  );

};

export default EditPostType;