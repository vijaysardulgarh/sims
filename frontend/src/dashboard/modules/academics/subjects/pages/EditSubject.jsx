// ============================================
// EDIT SUBJECT
// File: EditSubject.jsx
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

import SubjectForm from "../components/SubjectForm";
import subjectService from "../services/subjectService";

const EditSubject = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const [initialData,
    setInitialData] =
    useState({});

  useEffect(() => {

    fetchSubject();

  }, []);

  const fetchSubject = async () => {

    try {

      const response =
        await subjectService.getSubject(id);

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load subject"
      );
    }
  };

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await subjectService.updateSubject(
        id,
        data
      );

      toast.success(
        "Subject updated successfully"
      );

      navigate(
        "/dashboard/academics/subjects"
      );

    } catch (error) {

      toast.error(
        "Update failed"
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
        Edit Subject
      </h1>

      <SubjectForm
        initialData={initialData}
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>
  );
};

export default EditSubject;