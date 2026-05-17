// ============================================
// ADD CLASSROOM
// File: AddClassroom.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import ClassroomForm from "../components/ClassroomForm";

import classroomService from "../services/classroomService";

const AddClassroom = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await classroomService.createClassroom(
        data
      );

      toast.success(
        "Classroom created successfully"
      );

      navigate(
        "/dashboard/academics/classrooms"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create classroom"
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
          Add Classroom
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create new classroom
        </p>

      </div>

      <ClassroomForm
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>
  );
};

export default AddClassroom;