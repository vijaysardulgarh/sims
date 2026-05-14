import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast
from "react-hot-toast";

import ClassForm
from "../../../components/forms/academics/ClassForm";

import classService from "./classService";


const AddClass = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  // =========================
  // CREATE CLASS
  // =========================

  const handleSubmit = async (data) => {

    try {

      setLoading(true);

      await classService.createClass(data);

      toast.success(
        "Class created successfully"
      );

      navigate(
        "/dashboard/academics/classes"
      );

    } catch (error) {

      console.error(error);

      console.log(
        error.response?.data
      );
      
      toast.error(
      
        error.response?.data
      
          ? JSON.stringify(
              error.response.data
            )
      
          : "Failed to create class"
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

        Add Class

      </h1>

      <ClassForm

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default AddClass;