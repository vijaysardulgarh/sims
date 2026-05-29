import {
  useEffect,
  useState
} from "react";

import {
  Link
} from "react-router-dom";

import toast from "react-hot-toast";

import smcMemberService from "../services/smcMemberService";

const SMCMembersList = () => {

  // =====================================
  // STATE
  // =====================================

  const [members, setMembers] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  // =====================================
  // FETCH MEMBERS
  // =====================================

  const fetchMembers = async () => {

    try {

      setLoading(true);

      const response =
        await smcMemberService
          .getSMCMembers();

      setMembers(response);

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load SMC Members"
      );

    } finally {

      setLoading(false);

    }

  };

  // =====================================
  // LOAD DATA
  // =====================================

  useEffect(() => {

    fetchMembers();

  }, []);

  // =====================================
  // DELETE MEMBER
  // =====================================

  const handleDelete = async (
    id
  ) => {

    const confirmDelete =
      window.confirm(
        "Delete this SMC Member?"
      );

    if (!confirmDelete) {

      return;

    }

    try {

      await smcMemberService
        .deleteSMCMember(id);

      toast.success(
        "SMC Member Deleted"
      );

      fetchMembers();

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to delete member"
      );

    }

  };

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
  // UI
  // =====================================

  return (

    <div className="space-y-6">

      {/* ============================== */}
      {/* HEADER */}
      {/* ============================== */}

      <div className="
        flex
        items-center
        justify-between
      ">

        <div>

          <h1 className="
            text-3xl
            font-bold
            text-gray-800
          ">
            SMC Members
          </h1>

          <p className="
            text-gray-500
            mt-1
          ">
            School Management Committee Members
          </p>

        </div>

        <Link

          to="/dashboard/associations/smc-members/create"

          className="
            px-4
            py-2
            bg-blue-600
            text-white
            rounded-lg
          "
        >
          Add Member
        </Link>

      </div>

      {/* ============================== */}
      {/* TABLE */}
      {/* ============================== */}

      <div className="
        bg-white
        rounded-xl
        shadow
        overflow-hidden
      ">

        <table className="
          w-full
          border-collapse
        ">

          <thead>

            <tr className="
              bg-gray-100
              text-left
            ">

              <th className="p-3">
                Name
              </th>

              <th className="p-3">
                Position
              </th>

              <th className="p-3">
                Contact
              </th>

              <th className="p-3">
                Email
              </th>

              <th className="p-3">
                Website
              </th>

              <th className="p-3">
                Actions
              </th>

            </tr>

          </thead>

          <tbody>

            {

              members.length === 0

                ? (

                  <tr>

                    <td
                      colSpan="6"
                      className="
                        p-6
                        text-center
                        text-gray-500
                      "
                    >

                      No SMC Members Found

                    </td>

                  </tr>

                )

                : (

                  members.map(

                    (member) => (

                      <tr

                        key={member.id}

                        className="
                          border-t
                        "
                      >

                        <td className="p-3">
                          {member.name}
                        </td>

                        <td className="p-3">
                          {member.position}
                        </td>

                        <td className="p-3">
                          {
                            member.contact_number ||
                            "-"
                          }
                        </td>

                        <td className="p-3">
                          {
                            member.email ||
                            "-"
                          }
                        </td>

                        <td className="p-3">

                          {

                            member.show_on_website

                              ? "Yes"

                              : "No"

                          }

                        </td>

                        <td className="p-3">

                          <div className="
                            flex
                            gap-3
                          ">

                            <Link

                              to={`/dashboard/associations/smc-members/${member.id}`}

                              className="
                                text-blue-600
                                hover:underline
                              "
                            >
                              View
                            </Link>

                            <Link

                              to={`/dashboard/associations/smc-members/edit/${member.id}`}

                              className="
                                text-green-600
                                hover:underline
                              "
                            >
                              Edit
                            </Link>

                            <button

                              onClick={() =>
                                handleDelete(
                                  member.id
                                )
                              }

                              className="
                                text-red-600
                                hover:underline
                              "
                            >
                              Delete
                            </button>

                          </div>

                        </td>

                      </tr>

                    )

                  )

                )

            }

          </tbody>

        </table>

      </div>

    </div>

  );

};

export default SMCMembersList;