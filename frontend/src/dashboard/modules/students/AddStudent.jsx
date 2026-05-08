import { useState } from "react";

import { useNavigate } from "react-router-dom";

const AddStudent = () => {

  // =========================
  // NAVIGATION
  // =========================

  const navigate = useNavigate();

  // =========================
  // FORM STATE
  // =========================

  const [formData, setFormData] = useState({
    admissionNo: "",
    studentName: "",
    className: "",
    section: "",
    phone: "",
    status: "Active",
  });

  // =========================
  // HANDLE CHANGE
  // =========================

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

  };

  // =========================
  // HANDLE SUBMIT
  // =========================

  const handleSubmit = (e) => {

    e.preventDefault();

    // =========================
    // GET OLD STUDENTS
    // =========================

    const oldStudents =
      JSON.parse(
        localStorage.getItem("students")
      ) || [];

    // =========================
    // CREATE NEW STUDENT
    // =========================

    const newStudent = {
      id: Date.now(),

      admissionNo:
        formData.admissionNo,

      name:
        formData.studentName,

      class:
        formData.className,

      section:
        formData.section,

      phone:
        formData.phone,

      status:
        formData.status,
    };

    // =========================
    // SAVE NEW LIST
    // =========================

    const updatedStudents = [
      ...oldStudents,
      newStudent,
    ];

    localStorage.setItem(
      "students",
      JSON.stringify(updatedStudents)
    );

    // =========================
    // SUCCESS MESSAGE
    // =========================

    alert(
      "Student Added Successfully"
    );

    // =========================
    // REDIRECT
    // =========================

    navigate("/dashboard/students");

  };

  return (

    <div className="space-y-6">

      {/* PAGE HEADER */}
      <div>

        <h1 className="text-3xl font-bold text-gray-800">
          Add Student
        </h1>

        <p className="text-gray-500 mt-1">
          Create new student record
        </p>

      </div>

      {/* FORM */}
      <div className="bg-white rounded-2xl shadow p-8">

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-2 gap-6"
        >

          {/* Admission Number */}
          <div>

            <label className="block mb-2 font-medium text-gray-700">
              Admission Number
            </label>

            <input
              type="text"
              name="admissionNo"
              value={formData.admissionNo}
              onChange={handleChange}
              placeholder="Enter admission number"
              className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Student Name */}
          <div>

            <label className="block mb-2 font-medium text-gray-700">
              Student Name
            </label>

            <input
              type="text"
              name="studentName"
              value={formData.studentName}
              onChange={handleChange}
              placeholder="Enter student name"
              className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Class */}
          <div>

            <label className="block mb-2 font-medium text-gray-700">
              Class
            </label>

            <input
              type="text"
              name="className"
              value={formData.className}
              onChange={handleChange}
              placeholder="Enter class"
              className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Section */}
          <div>

            <label className="block mb-2 font-medium text-gray-700">
              Section
            </label>

            <input
              type="text"
              name="section"
              value={formData.section}
              onChange={handleChange}
              placeholder="Enter section"
              className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Phone */}
          <div>

            <label className="block mb-2 font-medium text-gray-700">
              Phone Number
            </label>

            <input
              type="text"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              placeholder="Enter phone number"
              className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Status */}
          <div>

            <label className="block mb-2 font-medium text-gray-700">
              Status
            </label>

            <select
              name="status"
              value={formData.status}
              onChange={handleChange}
              className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-600"
            >

              <option value="Active">
                Active
              </option>

              <option value="Inactive">
                Inactive
              </option>

            </select>

          </div>

          {/* BUTTON */}
          <div className="md:col-span-2">

            <button
              type="submit"
              className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-semibold transition"
            >
              Save Student
            </button>

          </div>

        </form>

      </div>

    </div>

  );

};

export default AddStudent;