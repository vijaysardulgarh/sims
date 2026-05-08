const StudentProfile = () => {

  // =========================
  // DUMMY STUDENT DATA
  // =========================

  const student = {
    admissionNo: "SIMS001",
    name: "Rahul Sharma",
    class: "10",
    section: "A",
    rollNo: "15",
    gender: "Male",
    dob: "12 March 2010",
    phone: "9876543210",
    email: "rahul@example.com",
    address: "Sirsa, Haryana",
    fatherName: "Ramesh Sharma",
    motherName: "Sunita Sharma",
    parentPhone: "9876543200",
    transport: "Bus Route 3",
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

              R

            </div>

          </div>

          {/* DETAILS */}
          <div className="flex-1 grid grid-cols-1 md:grid-cols-2 gap-6">

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