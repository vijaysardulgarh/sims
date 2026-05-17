// ============================================
// ADD SUBJECT
// File: AddSubject.jsx
// ============================================

import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import SubjectForm from "../components/SubjectForm";

// import subjectService from
// "../../../services/academics/subjectService";

import subjectService from "../services/subjectService";

const AddSubject = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await subjectService.createSubject(
        data
      );

      toast.success(
        "Subject created successfully"
      );

      navigate(
        "/dashboard/academics/subjects"
      );

    } catch (error) {

      toast.error(
        "Failed to create subject"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
      ">
        Add Subject
      </h1>

      <SubjectForm
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>
  );
};

export default AddSubject;