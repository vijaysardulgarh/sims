// ============================================
// ADD SECTION
// File: AddSection.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import SectionForm from "./SectionForm";

// import sectionService from
// "../../../services/academics/sectionService";

import sectionService from
"./sectionService";

const AddSection = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE SECTION
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await sectionService.createSection(
        data
      );

      toast.success(
        "Section created successfully"
      );

      navigate(
        "/dashboard/academics/sections"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create section"
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
          Add Section
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create new section
        </p>

      </div>

      <SectionForm
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>
  );
};

export default AddSection;