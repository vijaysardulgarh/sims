// ============================================
// EDIT CLASS INCHARGE
// File: EditClassIncharge.jsx
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

import ClassInchargeForm from "../components/ClassInchargeForm";

import classInchargeService from "../services/classInchargeService";

const EditClassIncharge = () => {

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

  const [initialData,
    setInitialData] =
    useState({});

  // ============================================
  // FETCH DATA
  // ============================================

  useEffect(() => {

    fetchClassIncharge();

  }, []);

  const fetchClassIncharge = async () => {

    try {

      const response =
        await classInchargeService.getClassIncharge(
          id
        );

      setInitialData(response);

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to load class incharge"
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

      await classInchargeService.updateClassIncharge(

        id,

        formData

      );

      toast.success(
        "Class Incharge Updated Successfully"
      );

      navigate(
        "/dashboard/staff/class-incharge"
      );

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to update class incharge"
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

  return (

    <div className="space-y-6">

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">

          Edit Class Incharge

        </h1>

        <p className="
          text-gray-500
          mt-1
        ">

          Update class incharge details

        </p>

      </div>

      <ClassInchargeForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default EditClassIncharge;