// ============================================
// ADD SANCTIONED POST
// File: AddSanctionedPost.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import SanctionedPostForm
from "./SanctionedPostForm";

import sanctionedPostService
from "./sanctionedPostService";

const AddSanctionedPost = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await sanctionedPostService.createSanctionedPost(

        formData

      );

      toast.success(
        "Sanctioned Post Added Successfully"
      );

      navigate(
        "/dashboard/staff/sanctioned-posts"
      );

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to add sanctioned post"
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

          Add Sanctioned Post

        </h1>

      </div>

      <SanctionedPostForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default AddSanctionedPost;