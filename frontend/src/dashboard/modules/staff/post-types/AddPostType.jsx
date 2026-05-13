// ============================================
// ADD POST TYPE
// File: AddPostType.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import PostTypeForm
from "./PostTypeForm";

import postTypeService
from "./postTypeService";

const AddPostType = () => {

  const navigate = useNavigate();

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
        "Post Type Added Successfully"
      );

      navigate(
        "/dashboard/staff/post-types"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to add post type"
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

          Add Post Type

        </h1>

        <p className="
          text-gray-500
          mt-1
        ">

          Create new staff post type

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