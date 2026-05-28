// ============================================
// TEACHER ATTENDANCE FORM
// File: TeacherAttendanceForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import staffService from "../services/teacherAttendanceService";

const TeacherAttendanceForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // STATES
  // ============================================

  const [staff, setStaff] =
    useState([]);

  const [formData, setFormData] =
    useState({

      staff: "",

      attendance_date: "",

      status: "Present",

      remarks: "",
    });

  // ============================================
  // FETCH STAFF
  // ============================================

  useEffect(() => {

    fetchStaff();

  }, []);

  const fetchStaff = async () => {

    try {

      const response =
        await staffService.getStaff();

      setStaff(

        Array.isArray(response)

          ? response

          : response.results || []
      );

    } catch (error) {

      console.log(error);
    }
  };

  // ============================================
  // PREFILL
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        staff:
          initialData.staff || "",

        attendance_date:
          initialData.attendance_date || "",

        status:
          initialData.status || "Present",

        remarks:
          initialData.remarks || "",
      });
    }

  }, [initialData]);

  // ============================================
  // HANDLE CHANGE
  // ============================================

  const handleChange = (e) => {

    const { name, value } = e.target;

    setFormData({

      ...formData,

      [name]: value,
    });
  };

  // ============================================
  // SUBMIT
  // ============================================

  const handleSubmit = (e) => {

    e.preventDefault();

    onSubmit(formData);
  };

  return (

    <form
      onSubmit={handleSubmit}
      className="
        bg-white
        rounded-2xl
        shadow
        p-6
        space-y-6
      "
    >

      {/* STAFF */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Staff
        </label>

        <select

          name="staff"

          value={formData.staff}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "

          required
        >

          <option value="">
            Select Staff
          </option>

          {

            staff.map((item) => (

              <option
                key={item.id}
                value={item.id}
              >

                {item.first_name}
                {" "}
                {item.last_name}

              </option>
            ))
          }

        </select>

      </div>

      {/* DATE */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Attendance Date
        </label>

        <input

          type="date"

          name="attendance_date"

          value={formData.attendance_date}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "

          required
        />

      </div>

      {/* STATUS */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Status
        </label>

        <select

          name="status"

          value={formData.status}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        >

          <option value="Present">
            Present
          </option>

          <option value="Absent">
            Absent
          </option>

          <option value="Leave">
            Leave
          </option>

        </select>

      </div>

      {/* REMARKS */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Remarks
        </label>

        <textarea

          name="remarks"

          value={formData.remarks}

          onChange={handleChange}

          rows="4"

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* BUTTON */}

      <button

        type="submit"

        disabled={loading}

        className="
          bg-blue-600
          hover:bg-blue-700
          text-white
          px-6
          py-3
          rounded-xl
        "
      >

        {loading

          ? "Saving..."

          : "Save Attendance"}

      </button>

    </form>
  );
};

export default TeacherAttendanceForm;