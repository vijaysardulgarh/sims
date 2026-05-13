// ============================================
// ADD CLASS SUBJECT
// File: AddClassSubject.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import ClassSubjectForm from "./ClassSubjectForm";

import classSubjectService from
"../../../services/academics/classSubjectService";

const AddClassSubject = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // ============================================
  // CREATE CLASS SUBJECT
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await classSubjectService.createClassSubject(
        data
      );

      toast.success(
        "Class subject created successfully"
      );

      navigate(
        "/dashboard/academics/class-subjects"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to create class subject"
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
          Add Class Subject
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Assign subjects to class
        </p>

      </div>

      <ClassSubjectForm

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default AddClassSubject;