import {
  useEffect,
  useState
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast
from "react-hot-toast";

import ClassForm
from "./ClassForm";

import classService from "./classService";


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

  }, []);

  const fetchClass = async () => {

    try {

      const response =
        await classService.getClass(id);

      setInitialData(response);

    } catch (error) {

      toast.error(
        "Failed to load class"
      );
    }
  };

  // =========================
  // UPDATE CLASS
  // =========================

  const handleSubmit = async (data) => {

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
        text-2xl
        font-bold
      ">

        Edit Class

      </h1>

      <ClassForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditClass;