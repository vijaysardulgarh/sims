import { useState } from "react";

import { useParams } from "react-router-dom";

const EditStudent = () => {

  // =========================
  // GET STUDENT ID
  // =========================

  const { id } = useParams();

  // =========================
  // DUMMY EXISTING DATA
  // =========================

  const [formData, setFormData] = useState({
    admissionNo: `SIMS00${id}`,
    studentName:
      id === "1"
        ? "Rahul Sharma"
        : "Priya Verma",
    className:
      id === "1"
        ? "10"
        : "9",
    section:
      id === "1"
        ? "A"
        : "B",
    phone:
      id === "1"
        ? "9876543210"
        : "9876543211",
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
  // HANDLE UPDATE
  // =========================

  const handleSubmit = (e) => {

    e.preventDefault();

    console.log(formData);

    alert(
      `Student ${id} Updated Successfully`
    );

  };

  return (

    <div className="space-y-6">

      {/* HEADER */}
      <div>

        <h1 className="text-3xl font-bold text-gray-800">
          Edit Student
        </h1>

        <p className="text-gray-500 mt-1">
          Update student details
        </p>

      </div>

      {/* FORM */}
      <div className="bg-white rounded-2xl shadow p-8">

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-2 gap-6"
        >

          {/* Student ID */}
          <div>

            <label className="block mb-2 font-medium text-gray-700">
              Student ID
            </label>

            <input
              type="text"
              value={id}
              disabled
              className="w-full bg-gray-100 border border-gray-300 rounded-xl px-4 py-3"
            />

          </div>

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
              className="bg-yellow-500 hover:bg-yellow-600 text-white px-6 py-3 rounded-xl font-semibold transition"
            >
              Update Student
            </button>

          </div>

        </form>

      </div>

    </div>

  );

};

export default EditStudent;