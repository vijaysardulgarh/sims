import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import AssociationMemberForm from "../components/AssociationMemberForm";
import associationMemberService from "../services/associationMemberService";

const AssociationMemberAddPage = () => {

  const navigate = useNavigate();

  const [loading,
    setLoading] =
    useState(false);

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await associationMemberService.create(
        data
      );

      toast.success(
        "Member created successfully"
      );

      navigate(
        "/dashboard/associations/association-members"
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Create failed"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="space-y-6">

      <h1 className="text-2xl font-bold">

        Add Member

      </h1>

      <AssociationMemberForm

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default AssociationMemberAddPage;