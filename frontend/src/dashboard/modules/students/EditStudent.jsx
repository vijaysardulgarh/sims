import {
  useEffect,
  useState,
} from "react";

import {
  useNavigate,
  useParams,
} from "react-router-dom";

import toast
from "react-hot-toast";

import StudentForm from
"../../components/forms/StudentForm";

import studentService from
"../../services/studentService";

const EditStudent = () => {

  // =====================================
  // PARAMS
  // =====================================

  const { id } = useParams();

  // =====================================
  // NAVIGATION
  // =====================================

  const navigate = useNavigate();

  // =====================================
  // STATES
  // =====================================

  const [student, setStudent] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  // =====================================
  // FETCH STUDENT
  // =====================================

  useEffect(() => {

    fetchStudent();

  }, []);

  const fetchStudent = async () => {

    try {

      const data =
        await studentService.getStudent(id);

      setStudent(data);

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to load student"
      );

    } finally {

      setLoading(false);

    }

  };

  // =====================================
  // UPDATE STUDENT
  // =====================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await studentService.updateStudent(

        id,

        formData

      );

      toast.success(
        "Student Updated Successfully"
      );

      navigate(
        "/dashboard/students"
      );

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to update student"
      );

    } finally {

      setLoading(false);

    }

  };

  // =====================================
  // LOADING
  // =====================================

  if (loading && !student) {

    return (

      <div className="p-10">

        <h1 className="
          text-2xl
          font-bold
        ">
          Loading...
        </h1>

      </div>

    );

  }

  // =====================================
  // UI
  // =====================================

  return (

    <div className="space-y-6">

      {/* HEADER */}

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Edit Student
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update student details
        </p>

      </div>

      {/* REUSABLE FORM */}

      <StudentForm

        initialData={student}

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>

  );

};

export default EditStudent;