// ============================================
// EDIT SECTION
// File: EditSection.jsx
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

import SectionForm from "../components/SectionForm";
import sectionService from "../services/sectionService";

const EditSection = () => {

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
  // FETCH SECTION
  // ============================================

  useEffect(() => {

    fetchSection();

  }, []);

  const fetchSection = async () => {

    try {

      const response =
        await sectionService.getSection(id);

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load section"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE SECTION
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await sectionService.updateSection(
        id,
        data
      );

      toast.success(
        "Section updated successfully"
      );

      navigate(
        "/dashboard/academics/sections"
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

        Loading section...

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
          Edit Section
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update section details
        </p>

      </div>

      <SectionForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditSection;