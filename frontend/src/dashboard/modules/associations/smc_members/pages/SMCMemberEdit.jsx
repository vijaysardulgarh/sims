import {
  useState,
  useEffect
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import SMCMemberForm from "../components/SMCMemberForm";

import smcMemberService from "../services/smcMemberService";

const SMCMemberEdit = () => {

  // =====================================
  // NAVIGATION
  // =====================================

  const navigate =
    useNavigate();

  const { id } =
    useParams();

  // =====================================
  // STATE
  // =====================================

  const [loading, setLoading] =
    useState(false);

  const [initialData,
    setInitialData] =
    useState({});

  const [pageLoading,
    setPageLoading] =
    useState(true);

  // =====================================
  // LOAD MEMBER
  // =====================================

  useEffect(() => {

    const fetchMember =
      async () => {

        try {

          const response =
            await smcMemberService
              .getSMCMember(id);

          setInitialData(
            response
          );

        } catch (error) {

          console.error(error);

          toast.error(
            "Failed to load member"
          );

        } finally {

          setPageLoading(false);

        }

      };

    fetchMember();

  }, [id]);

  // =====================================
  // UPDATE MEMBER
  // =====================================

  const handleSubmit =
    async (formData) => {

      try {

        setLoading(true);

        await smcMemberService
          .updateSMCMember(
            id,
            formData
          );

        toast.success(
          "SMC Member Updated Successfully"
        );

        navigate(
          "/dashboard/associations/smc-members"
        );

      } catch (error) {

        console.error(error);

        toast.error(
          "Update Failed"
        );

      } finally {

        setLoading(false);

      }

    };

  // =====================================
  // LOADING
  // =====================================

  if (pageLoading) {

    return (

      <div className="
        p-6
      ">
        Loading...
      </div>

    );

  }

  // =====================================
  // UI
  // =====================================

  return (

    <div className="space-y-6">

      {/* ============================= */}
      {/* PAGE HEADER */}
      {/* ============================= */}

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Edit SMC Member
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Update School Management Committee Member Information
        </p>

      </div>

      {/* ============================= */}
      {/* FORM */}
      {/* ============================= */}

      <SMCMemberForm

        initialData={initialData}

        onSubmit={handleSubmit}

        loading={loading}

      />

    </div>

  );

};

export default SMCMemberEdit;