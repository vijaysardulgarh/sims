// ============================================
// STAFF FORM
// File: StaffForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import postTypeService from "../../post-types/services/postTypeService";
import subjectService from "../../../academics/subjects/services/subjectService";

const StaffForm = ({
  initialData = {},
  onSubmit,
  loading = false,
}) => {

  const [postTypes, setPostTypes] =
    useState([]);

  const [subjects, setSubjects] =
    useState([]);

  const [formData, setFormData] =
    useState({

      employee_id: "",

      name: "",

      gender: "",

      father_name: "",

      mother_name: "",

      spouse_name: "",

      email: "",

      mobile_number: "",

      aadhar_number: "",

      post_type: "",

      staff_role: "Teaching",

      employment_type: "",

      subject: "",

      qualification: "",

      date_of_birth: "",

      joining_date: "",

      current_joining_date: "",

      retirement_date: "",

      priority: 1,

      max_periods_per_week: 40,

      category: "",

      bio: "",

      is_active: true,
    });

  useEffect(() => {

    fetchPostTypes();

    fetchSubjects();

  }, []);

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length
    ) {

      setFormData({

        employee_id:
          initialData.employee_id || "",

        name:
          initialData.name || "",

        gender:
          initialData.gender || "",

        father_name:
          initialData.father_name || "",

        mother_name:
          initialData.mother_name || "",

        spouse_name:
          initialData.spouse_name || "",

        email:
          initialData.email || "",

        mobile_number:
          initialData.mobile_number || "",

        aadhar_number:
          initialData.aadhar_number || "",

        post_type:
          initialData.post_type || "",

        staff_role:
          initialData.staff_role || "Teaching",

        employment_type:
          initialData.employment_type || "",

        subject:
          initialData.subject || "",

        qualification:
          initialData.qualification || "",

        date_of_birth:
          initialData.date_of_birth || "",

        joining_date:
          initialData.joining_date || "",

        current_joining_date:
          initialData.current_joining_date || "",

        retirement_date:
          initialData.retirement_date || "",

        priority:
          initialData.priority || 1,

        max_periods_per_week:
          initialData.max_periods_per_week || 40,

        category:
          initialData.category || "",

        bio:
          initialData.bio || "",

        is_active:
          initialData.is_active ?? true,
      });
    }

  }, [initialData]);

  const fetchPostTypes = async () => {

    try {

      const response =
        await postTypeService.getPostTypes();

      setPostTypes(

        Array.isArray(response)

          ? response

          : response.results || []
      );

    } catch (error) {

      console.log(error);
    }
  };

  const fetchSubjects = async () => {

    try {

      const response =
        await subjectService.getSubjects();

      setSubjects(

        Array.isArray(response)

          ? response

          : response.results || []
      );

    } catch (error) {

      console.log(error);
    }
  };

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

  const handleSubmit = (e) => {

    e.preventDefault();

    onSubmit(formData);
  };

  const inputClass =
    "w-full border rounded-xl px-4 py-3";

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

      <div className="
        grid
        grid-cols-1
        md:grid-cols-2
        gap-6
      ">

        <input
          name="employee_id"
          placeholder="Employee ID"
          value={formData.employee_id}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          className={inputClass}
          required
        />

        <select
          name="gender"
          value={formData.gender}
          onChange={handleChange}
          className={inputClass}
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

          <option value="Other">
            Other
          </option>

        </select>

        <input
          name="mobile_number"
          placeholder="Mobile Number"
          value={formData.mobile_number}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          name="aadhar_number"
          placeholder="Aadhaar Number"
          value={formData.aadhar_number}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          name="father_name"
          placeholder="Father Name"
          value={formData.father_name}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          name="mother_name"
          placeholder="Mother Name"
          value={formData.mother_name}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          name="spouse_name"
          placeholder="Spouse Name"
          value={formData.spouse_name}
          onChange={handleChange}
          className={inputClass}
        />

        <select
          name="post_type"
          value={formData.post_type}
          onChange={handleChange}
          className={inputClass}
        >
          <option value="">
            Select Post Type
          </option>

          {postTypes.map((item) => (

            <option
              key={item.id}
              value={item.id}
            >
              {item.name}
            </option>

          ))}

        </select>

        <select
          name="staff_role"
          value={formData.staff_role}
          onChange={handleChange}
          className={inputClass}
        >
          <option value="Teaching">
            Teaching
          </option>

          <option value="Non Teaching">
            Non Teaching
          </option>

          <option value="Admin">
            Admin
          </option>

          <option value="Support">
            Support
          </option>

        </select>

        <select
          name="employment_type"
          value={formData.employment_type}
          onChange={handleChange}
          className={inputClass}
        >
          <option value="">
            Select Employment Type
          </option>

          <option value="Regular">
            Regular
          </option>

          <option value="Contract">
            Contract
          </option>

          <option value="Guest">
            Guest
          </option>

          <option value="Part Time">
            Part Time
          </option>

        </select>

        <select
          name="subject"
          value={formData.subject}
          onChange={handleChange}
          className={inputClass}
        >
          <option value="">
            Select Subject
          </option>

          {subjects.map((item) => (

            <option
              key={item.id}
              value={item.id}
            >
              {item.name}
            </option>

          ))}

        </select>

        <input
          name="qualification"
          placeholder="Qualification"
          value={formData.qualification}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          type="date"
          name="date_of_birth"
          value={formData.date_of_birth}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          type="date"
          name="joining_date"
          value={formData.joining_date}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          type="date"
          name="current_joining_date"
          value={formData.current_joining_date}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          type="date"
          name="retirement_date"
          value={formData.retirement_date}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          type="number"
          name="priority"
          value={formData.priority}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          type="number"
          name="max_periods_per_week"
          value={formData.max_periods_per_week}
          onChange={handleChange}
          className={inputClass}
        />

        <input
          name="category"
          placeholder="Category"
          value={formData.category}
          onChange={handleChange}
          className={inputClass}
        />

      </div>

      <textarea
        name="bio"
        placeholder="Bio"
        value={formData.bio}
        onChange={handleChange}
        rows={4}
        className={inputClass}
      />

      <label className="flex items-center gap-2">

        <input
          type="checkbox"
          name="is_active"
          checked={formData.is_active}
          onChange={handleChange}
        />

        Active

      </label>

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
          : "Save Staff"}

      </button>

    </form>
  );
};

export default StaffForm;