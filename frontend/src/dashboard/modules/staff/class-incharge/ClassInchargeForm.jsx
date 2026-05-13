// ============================================
// CLASS INCHARGE FORM
// File: ClassInchargeForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import classService from
"../../academics/classes/classService";

import sectionService from
"../../academics/sections/sectionService";

import staffService from
"../staff/staffService";

const ClassInchargeForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // STATES
  // ============================================

  const [classes, setClasses] =
    useState([]);

  const [sections, setSections] =
    useState([]);

  const [staff, setStaff] =
    useState([]);

  const [formData, setFormData] =
    useState({

      student_class: "",

      section: "",

      staff: "",
    });

  // ============================================
  // FETCH DATA
  // ============================================

  useEffect(() => {

    fetchData();

  }, []);

  const fetchData = async () => {

    try {

      const [

        classResponse,

        sectionResponse,

        staffResponse,

      ] = await Promise.all([

        classService.getClasses(),

        sectionService.getSections(),

        staffService.getStaff(),
      ]);

      setClasses(

        Array.isArray(classResponse)

          ? classResponse

          : classResponse.results || []
      );

      setSections(

        Array.isArray(sectionResponse)

          ? sectionResponse

          : sectionResponse.results || []
      );

      setStaff(

        Array.isArray(staffResponse)

          ? staffResponse

          : staffResponse.results || []
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

        student_class:
          initialData.student_class || "",

        section:
          initialData.section || "",

        staff:
          initialData.staff || "",
      });
    }

  }, [initialData]);

  // ============================================
  // FILTERED SECTIONS
  // ============================================

  const filteredSections =
    sections.filter((section) =>

      String(
        section.student_class?.id ||

        section.student_class ||

        section.sec_class?.id ||

        section.sec_class
      )

      ===

      String(formData.student_class)
    );

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

      {/* CLASS */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Class
        </label>

        <select

          name="student_class"

          value={formData.student_class}

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
            Select Class
          </option>

          {

            classes.map((item) => (

              <option
                key={item.id}
                value={item.id}
              >

                {item.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* SECTION */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Section
        </label>

        <select

          name="section"

          value={formData.section}

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
            Select Section
          </option>

          {

            filteredSections.map((item) => (

              <option
                key={item.id}
                value={item.id}
              >

                {item.name}

              </option>
            ))
          }

        </select>

      </div>

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

          : "Save Class Incharge"}

      </button>

    </form>
  );
};

export default ClassInchargeForm;