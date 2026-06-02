import { useState, useEffect } from "react";


// =========================================
// INPUT FIELD COMPONENT
// =========================================

const InputField = ({
  label,
  name,
  type = "text",
  value,
  onChange,
  error,
}) => {

  return (

    <div>

      <label className="block mb-2 font-medium">
        {label}
      </label>

      <input
        type={type}
        name={name}
        value={value || ""}
        onChange={onChange}
        className="w-full border rounded-xl px-4 py-3"
      />

      {error && (
        <p className="text-red-500 text-sm mt-1">
          {error}
        </p>
      )}

    </div>
  );
};


// =========================================
// MAIN COMPONENT
// =========================================

const StudentForm = ({
  initialData = {},
  onSubmit,
  loading = false,
}) => {

  // =========================================
  // DROPDOWN STATES
  // =========================================

  const [classes, setClasses] = useState([]);
  const [streams, setStreams] = useState([]);
  const [sections, setSections] = useState([]);

  // =========================================
  // FORM STATE
  // =========================================

  const [formData, setFormData] = useState({

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
  // ERRORS
  // =========================================

  const [errors, setErrors] = useState({});

  // =========================================
  // LOAD DROPDOWNS
  // =========================================

  useEffect(() => {

    const fetchDropdowns = async () => {

      try {

        // CLASSES
        const classRes = await fetch(
          "http://127.0.0.1:8000/api/academics/classes/"
        );

        const classData = await classRes.json();

        setClasses(

          Array.isArray(classData)
        
            ? classData
        
            : classData.results || []
        );

        // STREAMS
        const streamRes = await fetch(
          "http://127.0.0.1:8000/api/academics/streams/"
        );

        const streamData = await streamRes.json();

        setStreams(

          Array.isArray(streamData)
        
            ? streamData
        
            : streamData.results || []
        );

        // SECTIONS
        const sectionRes = await fetch(
          "http://127.0.0.1:8000/api/academics/sections/"
        );

        const sectionData = await sectionRes.json();

        setSections(

          Array.isArray(sectionData)
        
            ? sectionData
        
            : sectionData.results || []
        );

      } catch (error) {

        console.log("DROPDOWN ERROR:", error);

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
  // FILTERED SECTIONS
  // =========================================

  const filteredSections = (

    Array.isArray(sections)
  
      ? sections
  
      : []
  
  ).filter((section) => {

    const sectionClassId =
      section.sec_class?.id ||
      section.sec_class ||
      section.class_obj?.id ||
      section.class_obj ||
      section.student_class?.id ||
      section.student_class ||
      section.class?.id ||
      section.class ||
      "";

    if (!formData.student_class) {
      return true;
    }

    return (
      String(sectionClassId) ===
      String(formData.student_class)
    );

  });

  // =========================================
  // HANDLE CHANGE
  // =========================================

  const handleChange = (e) => {

    const {
      name,
      value,
      type,
      checked,
    } = e.target;

    setFormData((prev) => ({

      ...prev,

      [name]:
        type === "checkbox"
          ? checked
          : value,

    }));
  };

  // =========================================
  // VALIDATION
  // =========================================

  const validate = () => {

    let newErrors = {};

    if (!formData.srn) {
      newErrors.srn = "SRN is required";
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

          <InputField
            label="SRN"
            name="srn"
            value={formData.srn}
            onChange={handleChange}
            error={errors.srn}
          />

          <InputField
            label="School"
            name="school"
            value={formData.school}
            onChange={handleChange}
          />

          <InputField
            label="School Code"
            name="school_code"
            value={formData.school_code}
            onChange={handleChange}
          />

          <InputField
            label="Admission Date"
            name="admission_date"
            type="date"
            value={formData.admission_date}
            onChange={handleChange}
          />

          <InputField
            label="Admission Number"
            name="admission_number"
            value={formData.admission_number}
            onChange={handleChange}
          />

          {/* CLASS */}

          <div>

            <label className="block mb-2 font-medium">
              Class
            </label>

            <select
              name="student_class"
              value={String(formData.student_class || "")}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            >

              <option value="">
                Select Class
              </option>


                {(Array.isArray(classes)
                  ? classes
                  : []
                ).map((item) => (

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
              value={String(formData.stream || "")}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            >

              <option value="">
                Select Stream
              </option>

              {(Array.isArray(streams)

                ? streams

                : []

              ).map((item) => (

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
              value={String(formData.section || "")}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            >

              <option value="">
                Select Section
              </option>


              {(Array.isArray(filteredSections)

              ? filteredSections

              : []

              ).map((item) => (

              <option
                key={item.id}
                value={String(item.id)}
              >

                {item.name}

                {item.stream?.name
                  ? ` (${item.stream.name})`
                  : ""}

              </option>

              ))}





            </select>

          </div>

          <InputField
            label="Roll Number"
            name="roll_number"
            type="number"
            value={formData.roll_number}
            onChange={handleChange}
          />

        </div>

      </div>

      {/* ===================================== */}
      {/* PERSONAL INFORMATION */}
      {/* ===================================== */}

      <div className="bg-white rounded-2xl shadow p-6">

        <h2 className="text-2xl font-bold mb-6">
          Personal Information
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          <InputField
            label="Student Name"
            name="full_name_aadhar"
            value={formData.full_name_aadhar}
            onChange={handleChange}
            error={errors.full_name_aadhar}
          />

          <InputField
            label="Date Of Birth"
            name="date_of_birth"
            type="date"
            value={formData.date_of_birth}
            onChange={handleChange}
          />

          {/* GENDER */}

          <div>

            <label className="block mb-2 font-medium">
              Gender
            </label>

            <select
              name="gender"
              value={formData.gender}
              onChange={handleChange}
              className="w-full border rounded-xl px-4 py-3"
            >

              <option value="">
                Select Gender
              </option>

              <option value="Male">
                Male
              </option>

              <option value="Female">
                Female
              </option>

            </select>

            {errors.gender && (
              <p className="text-red-500 text-sm mt-1">
                {errors.gender}
              </p>
            )}

          </div>

          <InputField
            label="Aadhaar Number"
            name="aadhaar_number"
            value={formData.aadhaar_number}
            onChange={handleChange}
          />

          <InputField
            label="Religion"
            name="religion"
            value={formData.religion}
            onChange={handleChange}
          />

          <InputField
            label="Category"
            name="category"
            value={formData.category}
            onChange={handleChange}
          />

          <InputField
            label="Caste"
            name="caste"
            value={formData.caste}
            onChange={handleChange}
          />

          <InputField
            label="Disability"
            name="disability"
            value={formData.disability}
            onChange={handleChange}
          />

        </div>

      </div>

      {/* ===================================== */}
      {/* PARENTS INFORMATION */}
      {/* ===================================== */}

      <div className="bg-white rounded-2xl shadow p-6">

        <h2 className="text-2xl font-bold mb-6">
          Parents Information
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          <InputField
            label="Father Name"
            name="father_full_name_aadhar"
            value={formData.father_full_name_aadhar}
            onChange={handleChange}
          />

          <InputField
            label="Father Aadhaar"
            name="father_aadhaar_number"
            value={formData.father_aadhaar_number}
            onChange={handleChange}
          />

          <InputField
            label="Father Mobile"
            name="father_mobile"
            value={formData.father_mobile}
            onChange={handleChange}
            error={errors.father_mobile}
          />

          <InputField
            label="Mother Name"
            name="mother_full_name_aadhar"
            value={formData.mother_full_name_aadhar}
            onChange={handleChange}
          />

          <InputField
            label="Mother Aadhaar"
            name="mother_aadhaar_number"
            value={formData.mother_aadhaar_number}
            onChange={handleChange}
          />

          <InputField
            label="Mother Mobile"
            name="mother_mobile"
            value={formData.mother_mobile}
            onChange={handleChange}
          />

        </div>

      </div>

      {/* ===================================== */}
      {/* FINANCIAL INFORMATION */}
      {/* ===================================== */}

      <div className="bg-white rounded-2xl shadow p-6">

        <h2 className="text-2xl font-bold mb-6">
          Financial Information
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          <InputField
            label="Family Annual Income"
            name="family_annual_income"
            value={formData.family_annual_income}
            onChange={handleChange}
          />

          <InputField
            label="Bank Name"
            name="bank_name"
            value={formData.bank_name}
            onChange={handleChange}
          />

          <InputField
            label="Account Number"
            name="account_number"
            value={formData.account_number}
            onChange={handleChange}
          />

          <InputField
            label="IFSC"
            name="ifsc"
            value={formData.ifsc}
            onChange={handleChange}
          />

          <InputField
            label="Family ID"
            name="family_id"
            value={formData.family_id}
            onChange={handleChange}
          />

        </div>

      </div>

      {/* ===================================== */}
      {/* ADDRESS INFORMATION */}
      {/* ===================================== */}

      <div className="bg-white rounded-2xl shadow p-6">

        <h2 className="text-2xl font-bold mb-6">
          Address Information
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          <InputField
            label="State"
            name="state"
            value={formData.state}
            onChange={handleChange}
          />

          <InputField
            label="District"
            name="district"
            value={formData.district}
            onChange={handleChange}
          />

          <InputField
            label="Block"
            name="block"
            value={formData.block}
            onChange={handleChange}
          />

          <InputField
            label="Sub District"
            name="sub_district"
            value={formData.sub_district}
            onChange={handleChange}
          />

          <InputField
            label="City / Village"
            name="city_village_town"
            value={formData.city_village_town}
            onChange={handleChange}
          />

          <InputField
            label="Postal Code"
            name="postal_code"
            value={formData.postal_code}
            onChange={handleChange}
          />

          <div className="md:col-span-2">

            <label className="block mb-2 font-medium">
              Address
            </label>

            <textarea
              name="address"
              value={formData.address || ""}
              onChange={handleChange}
              rows="4"
              className="w-full border rounded-xl px-4 py-3"
            />

          </div>

        </div>

      </div>

      {/* ===================================== */}
      {/* SUBJECTS */}
      {/* ===================================== */}

      <div className="bg-white rounded-2xl shadow p-6">

        <h2 className="text-2xl font-bold mb-6">
          Subjects
        </h2>

        <div>

          <label className="block mb-2 font-medium">
            Subjects Opted
          </label>

          <textarea
            name="subjects_opted"
            value={formData.subjects_opted || ""}
            onChange={handleChange}
            rows="4"
            className="w-full border rounded-xl px-4 py-3"
          />

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