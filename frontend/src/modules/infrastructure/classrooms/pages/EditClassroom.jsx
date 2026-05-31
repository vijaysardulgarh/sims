// ============================================
// EDIT CLASSROOM
// File: EditClassroom.jsx
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

import ClassroomForm from "../components/ClassroomForm";

import classroomService from "../services/classroomService";

const EditClassroom = () => {

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
  // FETCH CLASSROOM
  // ============================================

  useEffect(() => {

    fetchClassroom();

  }, []);

  const fetchClassroom = async () => {

    try {

      const response =
        await classroomService.getClassroom(
          id
        );

      setInitialData(
        response
      );

    } catch (error) {

      toast.error(
        "Failed to load classroom"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE CLASSROOM
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await classroomService.updateClassroom(
        id,
        data
      );

      toast.success(
        "Classroom updated successfully"
      );

      navigate(
        "/dashboard/infrastructure/classrooms"
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

        Loading classroom...

      </div>
    );
  }

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
          Edit Classroom
        </h1>

        <p
          className="
            text-gray-500
            mt-1
          "
        >
          Update classroom details
        </p>

      </div>

      <ClassroomForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditClassroom;