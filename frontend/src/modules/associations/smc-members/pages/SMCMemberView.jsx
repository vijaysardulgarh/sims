// ============================================
// IMPORTS
// ============================================

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

// ============================================
// COMPONENT
// ============================================

const SMCMemberView = () => {

    // ============================================
    // ROUTER
    // ============================================

    const { id } =
        useParams();

    const navigate =
        useNavigate();

    // ============================================
    // STATE
    // ============================================

    const [member, setMember] =
        useState(null);

    const [loading, setLoading] =
        useState(true);

    // ============================================
    // FETCH MEMBER
    // ============================================

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

    // ============================================
    // LOADING
    // ============================================

    if (loading) {

        return (

            <div className="p-6">

                Loading...

            </div>

        );

    }

    // ============================================
    // NOT FOUND
    // ============================================

    if (!member) {

        return (

            <div className="p-6">

                Member not found

            </div>

        );

    }

    // ============================================
    // UI
    // ============================================

    return (

        <div className="space-y-6">

            <div
                className="
                    bg-white
                    rounded-2xl
                    shadow
                    p-6
                "
            >

                {/* ======================================== */}
                {/* TITLE */}
                {/* ======================================== */}

                <h1
                    className="
                        text-3xl
                        font-bold
                        mb-6
                    "
                >
                    SMC Member Details
                </h1>

                {/* ======================================== */}
                {/* PHOTO */}
                {/* ======================================== */}

                {

                    member.photo && (

                        <div className="mb-6">

                            <img
                                src={member.photo}
                                alt={member.name}
                                className="
                                    w-32
                                    h-32
                                    rounded-xl
                                    object-cover
                                    border
                                "
                            />

                        </div>

                    )

                }

                {/* ======================================== */}
                {/* DETAILS */}
                {/* ======================================== */}

                <div
                    className="
                        grid
                        grid-cols-1
                        md:grid-cols-2
                        gap-6
                    "
                >

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
                            Gender:
                        </strong>

                        <p>
                            {member.gender || "-"}
                        </p>

                    </div>

                    <div>

                        <strong>
                            Category:
                        </strong>

                        <p>
                            {member.category || "-"}
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
                            Nomination Date:
                        </strong>

                        <p>
                            {
                                member.nomination_date ||
                                "-"
                            }
                        </p>

                    </div>

                    <div>

                        <strong>
                            Tenure End Date:
                        </strong>

                        <p>
                            {
                                member.tenure_end_date ||
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

                    <div className="md:col-span-2">

                        <strong>
                            Address:
                        </strong>

                        <p>
                            {
                                member.address ||
                                "-"
                            }
                        </p>

                    </div>

                </div>

                {/* ======================================== */}
                {/* REMARKS */}
                {/* ======================================== */}

                <div className="mt-6">

                    <strong>
                        Remarks:
                    </strong>

                    <p
                        className="
                            mt-2
                            text-gray-700
                            whitespace-pre-wrap
                        "
                    >
                        {
                            member.remarks ||
                            "-"
                        }
                    </p>

                </div>

                {/* ======================================== */}
                {/* ACTIONS */}
                {/* ======================================== */}

                <div
                    className="
                        mt-8
                        flex
                        gap-3
                    "
                >

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