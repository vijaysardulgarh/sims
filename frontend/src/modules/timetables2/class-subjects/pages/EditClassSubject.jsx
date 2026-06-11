// ============================================
// EDIT CLASS SUBJECT
// File: EditClassSubject.jsx
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

import ClassSubjectForm from "../components/ClassSubjectForm";

import classSubjectService from "../services/classSubjectService";

const EditClassSubject = () => {

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
  // FETCH CLASS SUBJECT
  // ============================================

  useEffect(() => {

    fetchClassSubject();

  }, []);

  const fetchClassSubject = async () => {

    try {

      const response =
        await classSubjectService.getClassSubject(
          id
        );

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load class subject"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE CLASS SUBJECT
  // ============================================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await classSubjectService.updateClassSubject(
        id,
        data
      );

      toast.success(
        "Class subject updated successfully"
      );

      navigate(
        "/dashboard/academics/class-subjects"
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

        Loading class subject...

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
          Edit Class Subject
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update class subject details
        </p>

      </div>

      <ClassSubjectForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditClassSubject;