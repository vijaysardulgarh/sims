// ============================================
// EDIT MEDIUM
// File: EditMedium.jsx
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

import MediumForm from "./MediumForm";

import mediumService from
"../../../services/academics/mediumService";

const EditMedium = () => {

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
  // FETCH MEDIUM
  // ============================================

  useEffect(() => {

    fetchMedium();

  }, []);

  const fetchMedium = async () => {

    try {

      const response =
        await mediumService.getMedium(id);

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load medium"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE MEDIUM
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await mediumService.updateMedium(
        id,
        data
      );

      toast.success(
        "Medium updated successfully"
      );

      navigate(
        "/dashboard/academics/mediums"
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

        Loading medium...

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
          Edit Medium
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update medium details
        </p>

      </div>

      <MediumForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditMedium;