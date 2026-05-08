import { useState } from "react";

import {
  useParams,
  useNavigate,
} from "react-router-dom";

const EditStudent = () => {

  // =========================
  // GET STUDENT ID
  // =========================

  const { id } = useParams();

  // =========================
  // NAVIGATION
  // =========================

  const navigate = useNavigate();

  // =========================
  // GET STUDENTS FROM STORAGE
  // =========================

  const students =
    JSON.parse(
      localStorage.getItem("students")
    ) || [];

  // =========================
  // FIND CURRENT STUDENT
  // =========================

  const existingStudent =
    students.find(
      (student) =>
        student.id === Number(id)
    );

  // =========================
  // STUDENT NOT FOUND
  // =========================

  if (!existingStudent) {

    return (

      <div className="p-10">

        <h1 className="text-3xl font-bold text-red-600">
          Student Not Found
        </h1>

      </div>

    );

  }

  // =========================
  // FORM STATE
  // =========================

  const [formData, setFormData] =
    useState({

      admissionNo:
        existingStudent.admissionNo,

      studentName:
        existingStudent.name,

      className:
        existingStudent.class,

      section:
        existingStudent.section,

      phone:
        existingStudent.phone,

      status:
        existingStudent.status,

    });

  // =========================
  // HANDLE CHANGE
  // =========================

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]:
        e.target.value,
    });

  };

  // =========================
  // HANDLE UPDATE
  // =========================

  const handleSubmit = (e) => {

    e.preventDefault();

    // =========================
    // UPDATE STUDENTS
    // =========================

    const updatedStudents =
      students.map((student) => {

        if (
          student.id === Number(id)
        ) {

          return {

            ...student,

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

        }

        return student;

      });

    // =========================
    // SAVE UPDATED DATA
    // =========================

    localStorage.setItem(
      "students",
      JSON.stringify(updatedStudents)
    );

    // =========================
    // SUCCESS MESSAGE
    // =========================

    alert(
      "Student Updated Successfully"
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
          Edit Student
        </h1>

        <p className="text-gray-500 mt-1">
          Update student details
        </p>

      </div>

      {/* FORM CARD */}
      <div className="bg-white rounded-2xl shadow p-8">

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-2 gap-6"
        >

          {/* STUDENT ID */}
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

          {/* ADMISSION NUMBER */}
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

          {/* STUDENT NAME */}
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

          {/* CLASS */}
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

          {/* SECTION */}
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

          {/* PHONE */}
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

          {/* STATUS */}
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

          {/* SUBMIT BUTTON */}
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