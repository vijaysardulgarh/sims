import { useParams } from "react-router-dom";

const StudentProfile = () => {

  // =========================
  // GET STUDENT ID FROM URL
  // =========================

  const { id } = useParams();

  // =========================
  // DUMMY STUDENT DATA
  // =========================

  const student = {
    id: id,
    admissionNo: `SIMS00${id}`,
    name:
      id === "1"
        ? "Rahul Sharma"
        : "Priya Verma",
    class:
      id === "1"
        ? "10"
        : "9",
    section:
      id === "1"
        ? "A"
        : "B",
    rollNo:
      id === "1"
        ? "15"
        : "22",
    gender:
      id === "1"
        ? "Male"
        : "Female",
    dob:
      id === "1"
        ? "12 March 2010"
        : "20 July 2011",
    phone:
      id === "1"
        ? "9876543210"
        : "9876543211",
    email:
      id === "1"
        ? "rahul@example.com"
        : "priya@example.com",
    address:
      id === "1"
        ? "Sirsa, Haryana"
        : "Delhi, India",
    fatherName:
      id === "1"
        ? "Ramesh Sharma"
        : "Amit Verma",
    motherName:
      id === "1"
        ? "Sunita Sharma"
        : "Pooja Verma",
    parentPhone:
      id === "1"
        ? "9876543200"
        : "9876543201",
    transport:
      id === "1"
        ? "Bus Route 3"
        : "Bus Route 1",
    hostel: "No",
    status: "Active",
  };

  return (

    <div className="space-y-6">

      {/* PAGE HEADER */}
      <div>

        <h1 className="text-3xl font-bold text-gray-800">
          Student Profile
        </h1>

        <p className="text-gray-500 mt-1">
          View complete student information
        </p>

      </div>

      {/* PROFILE CARD */}
      <div className="bg-white rounded-2xl shadow p-8">

        <div className="flex flex-col md:flex-row gap-8">

          {/* PHOTO */}
          <div className="flex justify-center">

            <div className="w-40 h-40 rounded-2xl bg-blue-100 flex items-center justify-center text-5xl font-bold text-blue-700">

              {student.name.charAt(0)}

            </div>

          </div>

          {/* DETAILS */}
          <div className="flex-1 grid grid-cols-1 md:grid-cols-2 gap-6">

            <ProfileItem
              label="Student ID"
              value={student.id}
            />

            <ProfileItem
              label="Admission No"
              value={student.admissionNo}
            />

            <ProfileItem
              label="Student Name"
              value={student.name}
            />

            <ProfileItem
              label="Class"
              value={student.class}
            />

            <ProfileItem
              label="Section"
              value={student.section}
            />

            <ProfileItem
              label="Roll Number"
              value={student.rollNo}
            />

            <ProfileItem
              label="Gender"
              value={student.gender}
            />

            <ProfileItem
              label="Date of Birth"
              value={student.dob}
            />

            <ProfileItem
              label="Phone"
              value={student.phone}
            />

            <ProfileItem
              label="Email"
              value={student.email}
            />

            <ProfileItem
              label="Father Name"
              value={student.fatherName}
            />

            <ProfileItem
              label="Mother Name"
              value={student.motherName}
            />

            <ProfileItem
              label="Parent Phone"
              value={student.parentPhone}
            />

            <ProfileItem
              label="Transport"
              value={student.transport}
            />

            <ProfileItem
              label="Hostel"
              value={student.hostel}
            />

            <ProfileItem
              label="Status"
              value={student.status}
            />

          </div>

        </div>

      </div>

      {/* EXTRA MODULES */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        {/* Attendance */}
        <div className="bg-white rounded-2xl shadow p-6">

          <h2 className="text-xl font-semibold text-gray-800 mb-3">
            Attendance
          </h2>

          <p className="text-4xl font-bold text-blue-600">
            92%
          </p>

        </div>

        {/* Fees */}
        <div className="bg-white rounded-2xl shadow p-6">

          <h2 className="text-xl font-semibold text-gray-800 mb-3">
            Fees Status
          </h2>

          <p className="text-4xl font-bold text-green-600">
            Paid
          </p>

        </div>

        {/* Exams */}
        <div className="bg-white rounded-2xl shadow p-6">

          <h2 className="text-xl font-semibold text-gray-800 mb-3">
            Latest Result
          </h2>

          <p className="text-4xl font-bold text-purple-600">
            A+
          </p>

        </div>

      </div>

    </div>

  );

};

// =========================
// PROFILE ITEM COMPONENT
// =========================

const ProfileItem = ({
  label,
  value,
}) => {

  return (

    <div>

      <p className="text-sm text-gray-500 mb-1">
        {label}
      </p>

      <p className="font-semibold text-gray-800">
        {value}
      </p>

    </div>

  );

};

export default StudentProfile;