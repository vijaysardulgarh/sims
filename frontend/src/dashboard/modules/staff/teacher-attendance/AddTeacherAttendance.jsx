// ============================================
// ADD TEACHER ATTENDANCE
// File: AddTeacherAttendance.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import TeacherAttendanceForm
from "./TeacherAttendanceForm";

import teacherAttendanceService
from "./teacherAttendanceService";

const AddTeacherAttendance = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await teacherAttendanceService.createTeacherAttendance(

        formData

      );

      toast.success(
        "Attendance Added Successfully"
      );

      navigate(
        "/dashboard/staff/teacher-attendance"
      );

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to add attendance"
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

          Add Teacher Attendance

        </h1>

      </div>

      <TeacherAttendanceForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default AddTeacherAttendance;