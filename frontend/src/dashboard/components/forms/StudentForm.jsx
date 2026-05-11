import { useState, useEffect } from "react";

const StudentForm = ({
  initialData = {},
  onSubmit,
  loading = false
}) => {

  // =========================================
  // DROPDOWN STATES
  // =========================================

  const [classes, setClasses] =
    useState([]);

  const [streams, setStreams] =
    useState([]);

  const [sections, setSections] =
    useState([]);

  // =========================================
  // FORM STATE
  // =========================================

  const [formData, setFormData] =
    useState({

      // Academic

      srn: "",

      school: "",

      school_code: "",

      admission_date: "",

      student_class: "",

      stream: "",

      section: "",

      roll_number: "",

      admission_number: "",

      // Personal

      full_name_aadhar: "",

      date_of_birth: "",

      gender: "",

      aadhaar_number: "",

      domicile_of_haryana: "",

      // Parents

      father_full_name_aadhar: "",

      father_aadhaar_number: "",

      mother_full_name_aadhar: "",

      mother_aadhaar_number: "",

      // Contact

      father_mobile: "",

      mother_mobile: "",

      // Financial

      family_annual_income: "",

      account_number: "",

      bank_name: "",

      ifsc: "",

      // Address

      state: "",

      district: "",

      block: "",

      sub_district: "",

      city_village_town: "",

      address: "",

      postal_code: "",

      // Subjects

      subjects_opted: "",

      subjects: "",

      // Other

      caste: "",

      category: "",

      disability: "",

      disorder: "",

      below_poverty_line_certificate_number: "",

      bpl_certificate_issuing_authority: "",

      family_id: "",

      religion: "",

      is_active: true,
    });

  // =========================================
  // FILTERED SECTIONS
  // =========================================

  const filteredSections =

    sections.filter(

      (section) =>

        String(section.class_obj) ===

        String(formData.student_class)
    );

  // =========================================
  // ERRORS
  // =========================================

  const [errors, setErrors] =
    useState({});

  // =========================================
  // LOAD DROPDOWNS
  // =========================================

  useEffect(() => {

    const fetchDropdowns = async () => {

      try {

        // =====================================
        // FETCH CLASSES
        // =====================================

        const classRes = await fetch(

          "http://127.0.0.1:8000/api/academics/classes/"
        );

        const classData =
          await classRes.json();

        setClasses(
          classData.results || classData
        );

        // =====================================
        // FETCH STREAMS
        // =====================================

        const streamRes = await fetch(

          "http://127.0.0.1:8000/api/academics/streams/"
        );

        const streamData =
          await streamRes.json();

        setStreams(
          streamData.results || streamData
        );

        // =====================================
        // FETCH SECTIONS
        // =====================================

        const sectionRes = await fetch(

          "http://127.0.0.1:8000/api/academics/sections/"
        );

        const sectionData =
          await sectionRes.json();

        setSections(
          sectionData.results || sectionData
        );

      } catch (error) {

        console.log(
          "DROPDOWN ERROR:",
          error
        );
      }
    };

    fetchDropdowns();

  }, []);

  // =========================================
  // LOAD INITIAL DATA
  // =========================================

  useEffect(() => {

    if (

      initialData &&

      Object.keys(initialData).length > 0
    ) {

      setFormData((prev) => ({

        ...prev,

        ...initialData,

        // =====================================
        // FIX RELATIONAL FIELDS
        // =====================================

        student_class: String(

          initialData.student_class?.id ||

          initialData.student_class ||

          initialData.student_class_id ||

          ""
        ),

        stream: String(

          initialData.stream?.id ||

          initialData.stream ||

          initialData.stream_id ||

          ""
        ),

        section: String(

          initialData.section?.id ||

          initialData.section ||

          initialData.section_id ||

          ""
        ),
      }));
    }

  }, [initialData]);

  // =========================================
  // HANDLE CHANGE
  // =========================================

  const handleChange = (e) => {

    const {
      name,
      value,
      type,
      checked
    } = e.target;

    setFormData({

      ...formData,

      [name]:

        type === "checkbox"

          ? checked

          : value,
    });
  };

  // =========================================
  // VALIDATION
  // =========================================

  const validate = () => {

    let newErrors = {};

    if (!formData.srn) {

      newErrors.srn =
        "SRN is required";
    }

    if (!formData.full_name_aadhar) {

      newErrors.full_name_aadhar =
        "Student name required";
    }

    if (!formData.student_class) {

      newErrors.student_class =
        "Class required";
    }

    if (!formData.gender) {

      newErrors.gender =
        "Gender required";
    }

    if (

      formData.father_mobile &&

      formData.father_mobile.length < 10
    ) {

      newErrors.father_mobile =
        "Invalid mobile number";
    }

    setErrors(newErrors);

    return (
      Object.keys(newErrors).length === 0
    );
  };

  // =========================================
  // HANDLE SUBMIT
  // =========================================

  const handleSubmit = (e) => {

    e.preventDefault();

    if (!validate()) return;

    onSubmit(formData);
  };

  // =========================================
  // UI
  // =========================================

  return (

    <form
      onSubmit={handleSubmit}
      className="space-y-10"
    >

      {/* ===================================== */}
      {/* ACADEMIC INFORMATION */}
      {/* ===================================== */}

      <div className="bg-white rounded-2xl shadow p-6">

        <h2 className="text-2xl font-bold mb-6">

          Academic Information

        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* SRN */}

          <div>

            <label className="block mb-2 font-medium">

              SRN

            </label>

            <input
              type="text"
              name="srn"
              value={formData.srn}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            />

            {errors.srn && (

              <p className="text-red-500 text-sm mt-1">

                {errors.srn}

              </p>
            )}

          </div>

          {/* SCHOOL CODE */}

          <div>

            <label className="block mb-2 font-medium">

              School Code

            </label>

            <input
              type="text"
              name="school_code"
              value={formData.school_code}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            />

          </div>

          {/* CLASS */}

          <div>

            <label className="block mb-2 font-medium">

              Class

            </label>

            <select
              name="student_class"
              value={formData.student_class}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            >

              <option value="">
                Select Class
              </option>

              {classes.map((item) => (

                <option
                  key={item.id}
                  value={String(item.id)}
                >

                  {item.name}

                </option>
              ))}

            </select>

            {errors.student_class && (

              <p className="text-red-500 text-sm mt-1">

                {errors.student_class}

              </p>
            )}

          </div>

          {/* STREAM */}

          <div>

            <label className="block mb-2 font-medium">

              Stream

            </label>

            <select
              name="stream"
              value={formData.stream}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            >

              <option value="">
                Select Stream
              </option>

              {streams.map((item) => (

                <option
                  key={item.id}
                  value={String(item.id)}
                >

                  {item.name}

                </option>
              ))}

            </select>

          </div>

          {/* SECTION */}

          <div>

            <label className="block mb-2 font-medium">

              Section

            </label>

            <select
              name="section"
              value={formData.section}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            >

              <option value="">
                Select Section
              </option>

              {filteredSections.map((item) => (

                <option
                  key={item.id}
                  value={String(item.id)}
                >

                  {item.name}

                </option>
              ))}

            </select>

          </div>

          {/* ROLL NUMBER */}

          <div>

            <label className="block mb-2 font-medium">

              Roll Number

            </label>

            <input
              type="number"
              name="roll_number"
              value={formData.roll_number}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            />

          </div>

        </div>

      </div>

      {/* SAVE BUTTON */}

      <div>

        <button
          type="submit"
          disabled={loading}
          className="
            bg-blue-600
            hover:bg-blue-700
            text-white
            px-8
            py-3
            rounded-xl
            font-semibold
          "
        >

          {loading
            ? "Saving..."
            : "Save Student"}

        </button>

      </div>

    </form>
  );
};

export default StudentForm;