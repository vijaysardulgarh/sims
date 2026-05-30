import { useState } from "react";

import { useNavigate }
from "react-router-dom";

import toast
from "react-hot-toast";

import StudentForm from
"../components/StudentForm";

import studentService from "../services/studentService";

const AddStudent = () => {

  // =====================================
  // NAVIGATION
  // =====================================

  const navigate = useNavigate();

  // =====================================
  // LOADING
  // =====================================

  const [loading, setLoading] =
    useState(false);

  // =====================================
  // HANDLE SUBMIT
  // =====================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      // ===============================
      // CREATE STUDENT
      // ===============================

      await studentService.createStudent(

        formData

      );

      // ===============================
      // SUCCESS
      // ===============================

      toast.success(
        "Student Added Successfully"
      );

      // ===============================
      // REDIRECT
      // ===============================

      navigate(
        "/dashboard/students"
      );

    } catch (error) {

      console.log(error);

      // ===============================
      // API ERROR HANDLING
      // ===============================

      if (
        error.response &&
        error.response.data
      ) {

        console.log(
          error.response.data
        );

      }

      console.log(
        "BACKEND ERROR:",
        error.response?.data
      );
      
      toast.error(
      
        error.response?.data
      
          ? JSON.stringify(
              error.response.data
            )
      
          : "Failed to add student"
      );

    } finally {

      setLoading(false);

    }

  };

  // =====================================
  // UI
  // =====================================

  return (

    <div className="space-y-6">

      {/* PAGE HEADER */}

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Add Student
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create new student record
        </p>

      </div>

      {/* FORM */}

      <StudentForm

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>

  );

};

export default AddStudent;