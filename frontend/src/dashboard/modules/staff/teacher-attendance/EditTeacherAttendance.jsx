// ============================================
// EDIT TEACHER ATTENDANCE
// File: EditTeacherAttendance.jsx
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

import TeacherAttendanceForm
from "./TeacherAttendanceForm";

import teacherAttendanceService
from "./teacherAttendanceService";

const EditTeacherAttendance = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(true);

  const [initialData,
    setInitialData] =
    useState({});

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchData();

  }, []);

  const fetchData = async () => {

    try {

      const response =
        await teacherAttendanceService.getTeacherAttendanceById(
          id
        );

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load data"
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

      await teacherAttendanceService.updateTeacherAttendance(

        id,

        formData

      );

      toast.success(
        "Updated Successfully"
      );

      navigate(
        "/dashboard/staff/teacher-attendance"
      );

    } catch (error) {

      toast.error(
        "Update Failed"
      );

    } finally {

      setLoading(false);
    }
  };

  if (loading && !initialData.id) {

    return (

      <div className="p-10">

        Loading...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
        text-gray-800
      ">

        Edit Teacher Attendance

      </h1>

      <TeacherAttendanceForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>
  );
};

export default EditTeacherAttendance;