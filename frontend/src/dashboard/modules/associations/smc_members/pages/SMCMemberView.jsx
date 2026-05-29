import {
  useState,
  useEffect
} from "react";

import {
  useParams,
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import smcMemberService from "../services/smcMemberService";

const SMCMemberView = () => {

  // =====================================
  // ROUTER
  // =====================================

  const { id } =
    useParams();

  const navigate =
    useNavigate();

  // =====================================
  // STATE
  // =====================================

  const [member, setMember] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  // =====================================
  // FETCH MEMBER
  // =====================================

  useEffect(() => {

    const fetchMember =
      async () => {

        try {

          const response =
            await smcMemberService
              .getSMCMember(id);

          setMember(
            response
          );

        } catch (error) {

          console.error(error);

          toast.error(
            "Failed to load member"
          );

        } finally {

          setLoading(false);

        }

      };

    fetchMember();

  }, [id]);

  // =====================================
  // LOADING
  // =====================================

  if (loading) {

    return (

      <div className="p-6">

        Loading...

      </div>

    );

  }

  // =====================================
  // NOT FOUND
  // =====================================

  if (!member) {

    return (

      <div className="p-6">

        Member not found

      </div>

    );

  }

  // =====================================
  // UI
  // =====================================

  return (

    <div className="space-y-6">

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <h1 className="
          text-3xl
          font-bold
          mb-6
        ">
          SMC Member Details
        </h1>

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          gap-6
        ">

          <div>

            <strong>
              Name:
            </strong>

            <p>
              {member.name || "-"}
            </p>

          </div>

          <div>

            <strong>
              Position:
            </strong>

            <p>
              {member.position || "-"}
            </p>

          </div>

          <div>

            <strong>
              Contact Number:
            </strong>

            <p>
              {
                member.contact_number ||
                "-"
              }
            </p>

          </div>

          <div>

            <strong>
              Email:
            </strong>

            <p>
              {
                member.email ||
                "-"
              }
            </p>

          </div>

          <div>

            <strong>
              Priority:
            </strong>

            <p>
              {
                member.priority ??
                "-"
              }
            </p>

          </div>

          <div>

            <strong>
              Show On Website:
            </strong>

            <p>

              {

                member.show_on_website

                  ? "Yes"

                  : "No"

              }

            </p>

          </div>

          <div>

            <strong>
              Status:
            </strong>

            <p>

              {

                member.is_active

                  ? "Active"

                  : "Inactive"

              }

            </p>

          </div>

        </div>

        {/* ========================= */}
        {/* ACTIONS */}
        {/* ========================= */}

        <div className="
          mt-8
          flex
          gap-3
        ">

          <button

            onClick={() =>
              navigate(
                "/dashboard/associations/smc-members"
              )
            }

            className="
              bg-gray-600
              hover:bg-gray-700
              text-white
              px-6
              py-3
              rounded-xl
            "
          >
            Back
          </button>

          <button

            onClick={() =>
              navigate(
                `/dashboard/associations/smc-members/edit/${id}`
              )
            }

            className="
              bg-blue-600
              hover:bg-blue-700
              text-white
              px-6
              py-3
              rounded-xl
            "
          >
            Edit
          </button>

        </div>

      </div>

    </div>

  );

};

export default SMCMemberView;