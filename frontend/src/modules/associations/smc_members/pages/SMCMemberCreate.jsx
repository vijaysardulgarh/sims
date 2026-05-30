import { useState } from "react";

import { useNavigate }
from "react-router-dom";

import toast
from "react-hot-toast";

import SMCMemberForm
from "../components/SMCMemberForm";

import smcMemberService
from "../services/smcMemberService";

const SMCMemberCreate = () => {

  // =====================================
  // NAVIGATION
  // =====================================

  const navigate =
    useNavigate();

  // =====================================
  // LOADING
  // =====================================

  const [loading, setLoading] =
    useState(false);

  // =====================================
  // SUBMIT
  // =====================================

  const handleSubmit = async (
    formData
  ) => {

    try {

      setLoading(true);

      await smcMemberService
        .createSMCMember(
          formData
        );

      toast.success(
        "SMC Member Added Successfully"
      );

      navigate(
        "/dashboard/associations/smc-members"
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to add member"
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

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Add SMC Member
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Create a new School Management Committee Member
        </p>

      </div>

      <SMCMemberForm
        onSubmit={handleSubmit}
        loading={loading}
      />

    </div>

  );

};

export default SMCMemberCreate;