import {
  useEffect,
  useState
} from "react";

import {
  useParams,
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import studentService from "./studentService";


const StudentProfile = () => {

  // =====================================
  // PARAMS
  // =====================================

  const { id } = useParams();

  const navigate = useNavigate();

  // =====================================
  // STATES
  // =====================================

  const [student, setStudent] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  // =====================================
  // FETCH STUDENT
  // =====================================

  useEffect(() => {

    fetchStudent();

  }, [id]);

  const fetchStudent = async () => {

    try {

      setLoading(true);

      const data =
        await studentService.getStudent(id);

      setStudent(data);

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load student"
      );

    } finally {

      setLoading(false);
    }
  };

  // =====================================
  // LOADING
  // =====================================

  if (loading) {

    return (

      <div className="p-6">

        Loading student profile...

      </div>
    );
  }

  // =====================================
  // NO STUDENT
  // =====================================

  if (!student) {

    return (

      <div className="p-6">

        Student not found

      </div>
    );
  }

  return (

    <div className="space-y-6">

      {/* ================================= */}
      {/* HEADER */}
      {/* ================================= */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
        flex
        flex-col
        md:flex-row
        justify-between
        gap-4
      ">

        <div>

          <h1 className="
            text-3xl
            font-bold
            text-gray-800
          ">

            {student.full_name_aadhar}

          </h1>

          <p className="text-gray-500 mt-2">

            SRN: {student.srn}

          </p>

        </div>

        <div className="flex gap-3">

          <button
            onClick={() =>
              navigate(
                `/dashboard/students/edit/${student.srn}`
              )
            }
            className="
              bg-blue-600
              hover:bg-blue-700
              text-white
              px-5
              py-2
              rounded-xl
              font-medium
            "
          >

            Edit Student

          </button>

          <button
            onClick={() =>
              navigate(
                "/dashboard/students"
              )
            }
            className="
              border
              px-5
              py-2
              rounded-xl
              font-medium
            "
          >

            Back

          </button>

        </div>

      </div>

      {/* ================================= */}
      {/* ACADEMIC INFO */}
      {/* ================================= */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <h2 className="
          text-2xl
          font-bold
          mb-6
        ">

          Academic Information

        </h2>

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          gap-6
        ">

          <ProfileItem
            label="School Code"
            value={student.school_code}
          />

          <ProfileItem
            label="Admission Number"
            value={student.admission_number}
          />

          <ProfileItem
            label="Roll Number"
            value={student.roll_number}
          />

          <ProfileItem
            label="Class"
            value={
              student.student_class_data?.name
            }
          />

          <ProfileItem
            label="Section"
            value={
              student.section_data?.name
            }
          />

          <ProfileItem
            label="Stream"
            value={
              student.stream_data?.name
            }
          />

          <ProfileItem
            label="Medium"
            value={
              student.medium_data?.name
            }
          />

          <ProfileItem
            label="Status"
            value={
              student.is_active
                ? "Active"
                : "Inactive"
            }
          />

        </div>

      </div>

      {/* ================================= */}
      {/* PERSONAL INFO */}
      {/* ================================= */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <h2 className="
          text-2xl
          font-bold
          mb-6
        ">

          Personal Information

        </h2>

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          gap-6
        ">

          <ProfileItem
            label="Full Name"
            value={student.full_name_aadhar}
          />

          <ProfileItem
            label="Date of Birth"
            value={student.date_of_birth}
          />

          <ProfileItem
            label="Gender"
            value={student.gender}
          />

          <ProfileItem
            label="Aadhaar Number"
            value={student.aadhaar_number}
          />

          <ProfileItem
            label="Religion"
            value={student.religion}
          />

          <ProfileItem
            label="Category"
            value={student.category}
          />

          <ProfileItem
            label="Family ID"
            value={student.family_id}
          />

        </div>

      </div>

      {/* ================================= */}
      {/* PARENTS INFO */}
      {/* ================================= */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <h2 className="
          text-2xl
          font-bold
          mb-6
        ">

          Parent Information

        </h2>

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          gap-6
        ">

          <ProfileItem
            label="Father Name"
            value={
              student.father_full_name_aadhar
            }
          />

          <ProfileItem
            label="Mother Name"
            value={
              student.mother_full_name_aadhar
            }
          />

          <ProfileItem
            label="Father Mobile"
            value={student.father_mobile}
          />

          <ProfileItem
            label="Mother Mobile"
            value={student.mother_mobile}
          />

        </div>

      </div>

      {/* ================================= */}
      {/* ADDRESS INFO */}
      {/* ================================= */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <h2 className="
          text-2xl
          font-bold
          mb-6
        ">

          Address Information

        </h2>

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          gap-6
        ">

          <ProfileItem
            label="State"
            value={student.state}
          />

          <ProfileItem
            label="District"
            value={student.district}
          />

          <ProfileItem
            label="Block"
            value={student.block}
          />

          <ProfileItem
            label="City"
            value={student.city_village_town}
          />

          <ProfileItem
            label="Postal Code"
            value={student.postal_code}
          />

          <ProfileItem
            label="Address"
            value={student.address}
          />

        </div>

      </div>

    </div>
  );
};


// =========================================
// PROFILE ITEM
// =========================================

const ProfileItem = ({
  label,
  value
}) => {

  return (

    <div>

      <p className="
        text-sm
        text-gray-500
        mb-1
      ">

        {label}

      </p>

      <p className="
        text-lg
        font-semibold
        text-gray-800
      ">

        {value || "-"}

      </p>

    </div>
  );
};

export default StudentProfile;