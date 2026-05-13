// ============================================
// STAFF PROFILE
// File: StaffProfile.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useParams,
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import staffService from "./staffService";

const StaffProfile = () => {

  // ============================================
  // PARAMS
  // ============================================

  const { id } = useParams();

  const navigate = useNavigate();

  // ============================================
  // STATES
  // ============================================

  const [staff, setStaff] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH STAFF
  // ============================================

  useEffect(() => {

    fetchStaff();

  }, []);

  const fetchStaff = async () => {

    try {

      const response =
        await staffService.getStaffMember(
          id
        );

      setStaff(response);

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to load staff profile"
      );

    } finally {

      setLoading(false);
    }
  };

  // ============================================
  // LOADING
  // ============================================

  if (loading) {

    return (

      <div className="p-6">

        Loading profile...

      </div>
    );
  }

  // ============================================
  // NO DATA
  // ============================================

  if (!staff) {

    return (

      <div className="p-6">

        Staff not found

      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      {/* HEADER */}

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

            Staff Profile

          </h1>

          <p className="
            text-gray-500
            mt-1
          ">

            Complete staff details

          </p>

        </div>

        <button

          onClick={() =>
            navigate(
              `/dashboard/staff/staff/edit/${staff.id}`
            )
          }

          className="
            bg-blue-600
            text-white
            px-5
            py-2
            rounded-xl
            hover:bg-blue-700
          "
        >

          Edit Profile

        </button>

      </div>

      {/* PROFILE CARD */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        overflow-hidden
      ">

        {/* TOP SECTION */}

        <div className="
          bg-gradient-to-r
          from-blue-600
          to-indigo-600
          p-8
          text-white
        ">

          <div className="
            flex
            flex-col
            md:flex-row
            items-center
            gap-6
          ">

            {/* IMAGE */}

            <img

              src={
                staff.profile_picture ||

                "https://via.placeholder.com/150"
              }

              alt="Profile"

              className="
                h-36
                w-36
                rounded-full
                object-cover
                border-4
                border-white
              "
            />

            {/* INFO */}

            <div>

              <h2 className="
                text-4xl
                font-bold
              ">

                {staff.name ||

                  `${staff.first_name || ""}
                   ${staff.last_name || ""}`
                }

              </h2>

              <p className="
                mt-2
                text-lg
              ">

                {staff.designation ||
                  staff.post_type_name}

              </p>

              <div className="
                mt-4
                flex
                flex-wrap
                gap-3
              ">

                <span className="
                  bg-white/20
                  px-4
                  py-1
                  rounded-full
                  text-sm
                ">

                  Employee ID:
                  {" "}
                  {staff.employee_id || "-"}

                </span>

                <span className="
                  bg-white/20
                  px-4
                  py-1
                  rounded-full
                  text-sm
                ">

                  {staff.staff_role || "-"}

                </span>

              </div>

            </div>

          </div>

        </div>

        {/* DETAILS */}

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          gap-6
          p-8
        ">

          {/* PERSONAL */}

          <div className="
            space-y-4
          ">

            <h3 className="
              text-xl
              font-bold
              text-gray-800
              border-b
              pb-2
            ">

              Personal Details

            </h3>

            <ProfileItem
              label="Father Name"
              value={staff.father_name}
            />

            <ProfileItem
              label="Mother Name"
              value={staff.mother_name}
            />

            <ProfileItem
              label="Gender"
              value={staff.gender}
            />

            <ProfileItem
              label="Date of Birth"
              value={staff.date_of_birth}
            />

            <ProfileItem
              label="Aadhar Number"
              value={staff.aadhar_number}
            />

          </div>

          {/* PROFESSIONAL */}

          <div className="
            space-y-4
          ">

            <h3 className="
              text-xl
              font-bold
              text-gray-800
              border-b
              pb-2
            ">

              Professional Details

            </h3>

            <ProfileItem
              label="Qualification"
              value={staff.qualification}
            />

            <ProfileItem
              label="Subject"
              value={staff.subject_name}
            />

            <ProfileItem
              label="Joining Date"
              value={staff.joining_date}
            />

            <ProfileItem
              label="Employment Type"
              value={staff.employment_type}
            />

            <ProfileItem
              label="Max Periods"
              value={
                staff.max_periods_per_week
              }
            />

          </div>

          {/* CONTACT */}

          <div className="
            space-y-4
          ">

            <h3 className="
              text-xl
              font-bold
              text-gray-800
              border-b
              pb-2
            ">

              Contact Details

            </h3>

            <ProfileItem
              label="Email"
              value={staff.email}
            />

            <ProfileItem
              label="Mobile"
              value={staff.mobile_number}
            />

          </div>

          {/* STATUS */}

          <div className="
            space-y-4
          ">

            <h3 className="
              text-xl
              font-bold
              text-gray-800
              border-b
              pb-2
            ">

              Status

            </h3>

            <ProfileItem
              label="Active"
              value={
                staff.is_active
                  ? "Yes"
                  : "No"
              }
            />

            <ProfileItem
              label="Priority"
              value={staff.priority}
            />

            <ProfileItem
              label="Retirement Date"
              value={staff.retirement_date}
            />

          </div>

        </div>

      </div>

    </div>
  );
};

// ============================================
// PROFILE ITEM COMPONENT
// ============================================

const ProfileItem = ({

  label,

  value

}) => {

  return (

    <div>

      <p className="
        text-sm
        text-gray-500
      ">

        {label}

      </p>

      <p className="
        text-base
        font-medium
        text-gray-800
      ">

        {value || "-"}

      </p>

    </div>
  );
};

export default StaffProfile;