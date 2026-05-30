import {
  useEffect,
  useState
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import ClassForm from "../components/ClassForm";

import classService from "../services/classService";


const EditClass = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const [initialData,
    setInitialData] =
    useState({});

  // =========================
  // FETCH CLASS
  // =========================

  useEffect(() => {

    fetchClass();

  }, [id]);

  const fetchClass = async () => {

    try {

      setLoading(true);

      const response =
        await classService.getClass(
          id
        );

      setInitialData(
        response
      );

    } catch (error) {

      console.error(
        error
      );

      toast.error(
        "Failed to load class"
      );

    } finally {

      setLoading(false);
    }
  };

  // =========================
  // UPDATE CLASS
  // =========================

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await classService.updateClass(
        id,
        data
      );

      toast.success(
        "Class updated successfully"
      );

      navigate(
        "/dashboard/academics/classes"
      );

    } catch (error) {

      console.error(
        error
      );

      console.log(
        error.response?.data
      );

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

  return (

    <div className="space-y-6">

      <h1
        className="
          text-2xl
          font-bold
        "
      >

        Edit Class

      </h1>

      <ClassForm

        initialData={
          initialData
        }

        onSubmit={
          handleSubmit
        }

        loading={
          loading
        }
      />

    </div>
  );
};

export default EditClass;