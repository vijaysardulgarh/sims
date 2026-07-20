// ============================================
// ADD POST TYPE
// File: AddPostType.jsx
// ============================================

import {
  useState,
} from "react";

import {
  useNavigate,
} from "react-router-dom";

import toast from "react-hot-toast";

import PostTypeForm from "../components/PostTypeForm";
import postTypeService from "../services/postTypeService";

const AddPostType = () => {

  // ============================================
  // NAVIGATION
  // ============================================

  const navigate = useNavigate();

  // ============================================
  // STATE
  // ============================================

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE
  // ============================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await postTypeService.createPostType(
        formData
      );

      toast.success(
        "Post Type added successfully."
      );

      navigate(
        "/dashboard/staff/post-types"
      );

    } catch (error) {

      console.error(error);

      if (error.response?.data) {

        const errors =
          Object.entries(error.response.data)
            .map(([field, messages]) =>
              `${field}: ${Array.isArray(messages) ? messages.join(", ") : messages}`
            )
            .join("\n");

        toast.error(errors);

      } else {

        toast.error(
          "Failed to add post type."
        );

      }

    } finally {

      setLoading(false);

    }

  };

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

          Add Post Type

        </h1>

        <p
          className="
            text-gray-500
            mt-1
          "
        >

          Create a new staff post type.

        </p>

      </div>

      <PostTypeForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>

  );

};

export default AddPostType;