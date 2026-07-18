// ============================================
// STAFF FORM
// ============================================

import { useEffect, useState } from "react";
import postTypeService from "../../post-types/services/postTypeService";
import subjectService from "../../../academics/subjects/services/subjectService";

const StaffForm = ({ initialData = {}, onSubmit, loading = false }) => {
  const [postTypes, setPostTypes] = useState([]);
  const [subjects, setSubjects] = useState([]);

  // ============================================
  // FORM DATA
  // ============================================
  const [formData, setFormData] = useState({
    // BASIC
    employee_id: "",
    name: "",
    profile_picture: null,
    gender: "",

    // FAMILY
    father_name: "",
    mother_name: "",
    spouse_name: "",

    // EMPLOYMENT
    post_type: "",
    designation: "",
    staff_role: "Teaching",
    employment_type: "",
    status: "Active",
    subject: "",
    qualification: "",
    teaching_experience_years: 0,
    priority: 1,
    min_periods_per_week: 20,
    max_periods_per_week: 40,
    is_class_teacher: false,
    is_house_incharge: false,

    // CONTACT
    mobile_number: "",
    email: "",
    aadhar_number: "",

    // ADDRESS
    address: "",
    city: "",
    state: "",
    pin_code: "",

    // DATES
    date_of_birth: "",
    joining_date: "",
    current_joining_date: "",
    retirement_date: "",

    // OTHER
    category: "",
    bio: "",
    is_active: true,
  });

  // ============================================
  // LOAD DROPDOWNS
  // ============================================
  useEffect(() => {
    fetchPostTypes();
    fetchSubjects();
  }, []);

  // ============================================
  // EDIT MODE
  // ============================================
  useEffect(() => {
    if (initialData && Object.keys(initialData).length) {
      setFormData({
        employee_id: initialData.employee_id || "",
        name: initialData.name || "",
        profile_picture: null,
        gender: initialData.gender || "",
        father_name: initialData.father_name || "",
        mother_name: initialData.mother_name || "",
        spouse_name: initialData.spouse_name || "",
        post_type: initialData.post_type || "",
        designation: initialData.designation || "",
        staff_role: initialData.staff_role || "Teaching",
        employment_type: initialData.employment_type || "",
        status: initialData.status || "Active",
        subject: initialData.subject || "",
        qualification: initialData.qualification || "",
        teaching_experience_years: initialData.teaching_experience_years || 0,
        priority: initialData.priority || 1,
        min_periods_per_week: initialData.min_periods_per_week || 20,
        max_periods_per_week: initialData.max_periods_per_week || 40,
        is_class_teacher: initialData.is_class_teacher ?? false,
        is_house_incharge: initialData.is_house_incharge ?? false,
        mobile_number: initialData.mobile_number || "",
        email: initialData.email || "",
        aadhar_number: initialData.aadhar_number || "",
        address: initialData.address || "",
        city: initialData.city || "",
        state: initialData.state || "",
        pin_code: initialData.pin_code || "",
        date_of_birth: initialData.date_of_birth || "",
        joining_date: initialData.joining_date || "",
        current_joining_date: initialData.current_joining_date || "",
        retirement_date: initialData.retirement_date || "",
        category: initialData.category || "",
        bio: initialData.bio || "",
        is_active: initialData.is_active ?? true,
      });
    }
  }, [initialData]);

  // ============================================
  // FETCH POST TYPES
  // ============================================
  const fetchPostTypes = async () => {
    try {
      const response = await postTypeService.getPostTypes();
      setPostTypes(Array.isArray(response) ? response : response.results || []);
    } catch (error) {
      console.log(error);
    }
  };

  // ============================================
  // FETCH SUBJECTS
  // ============================================
  const fetchSubjects = async () => {
    try {
      const response = await subjectService.getSubjects();
      setSubjects(Array.isArray(response) ? response : response.results || []);
    } catch (error) {
      console.log(error);
    }
  };

  // ============================================
  // HANDLE CHANGE
  // ============================================
  const handleChange = (e) => {
    const { name, value, type, checked, files } = e.target;
    setFormData({
      ...formData,
      [name]:
        type === "checkbox"
          ? checked
          : type === "file"
          ? files[0]
          : value,
    });
  };

  // ============================================
  // SUBMIT
  // ============================================
  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.name.trim()) {
      alert("Staff Name is required.");
      return;
    }

    if (!formData.employee_id.trim()) {
      alert("Employee ID is required.");
      return;
    }

    if (formData.mobile_number && formData.mobile_number.length !== 10) {
      alert("Enter a valid 10 digit mobile number.");
      return;
    }

    if (formData.aadhar_number && formData.aadhar_number.length !== 12) {
      alert("Enter a valid 12 digit Aadhaar number.");
      return;
    }

    if (
      formData.staff_role === "Teaching" &&
      Number(formData.min_periods_per_week) > Number(formData.max_periods_per_week)
    ) {
      alert("Minimum periods cannot be greater than Maximum periods.");
      return;
    }

    if (
      formData.joining_date &&
      formData.retirement_date &&
      formData.retirement_date <= formData.joining_date
    ) {
      alert("Retirement Date must be after Joining Date.");
      return;
    }

    const data = new FormData();
    Object.entries(formData).forEach(([key, value]) => {
      if (value !== null && value !== undefined) {
        data.append(key, value);
      }
    });

    onSubmit(data);
  };

  const inputClass = "w-full border rounded-xl px-4 py-3";

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white rounded-2xl shadow p-6 space-y-8"
    >
      {/* ============================================
          BASIC INFORMATION
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Basic Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">
          <input
            name="employee_id"
            placeholder="Employee ID"
            value={formData.employee_id}
            onChange={handleChange}
            className={inputClass}
          />
          <input
            name="name"
            placeholder="Staff Name"
            value={formData.name}
            onChange={handleChange}
            className={inputClass}
            required
          />
          
          {/* Profile Picture Upload & Preview */}
          <div className="flex items-center gap-4">
            <input
              type="file"
              name="profile_picture"
              onChange={handleChange}
              className={inputClass}
              accept="image/*"
            />
            {formData.profile_picture && (
              <img
                src={URL.createObjectURL(formData.profile_picture)}
                alt="Preview"
                className="h-12 w-12 rounded-full object-cover shadow-sm shrink-0"
              />
            )}
          </div>

          <select
            name="gender"
            value={formData.gender}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>
        </div>
      </div>

      {/* ============================================
          FAMILY INFORMATION
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Family Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
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
        </div>
      </div>

      {/* ============================================
          EMPLOYMENT INFORMATION
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Employment Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <select
            name="post_type"
            value={formData.post_type}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="">Select Post Type</option>
            {postTypes.map((item) => (
              <option key={item.id} value={item.id}>
                {item.name}
              </option>
            ))}
          </select>
          <input
            name="designation"
            placeholder="Designation"
            value={formData.designation}
            onChange={handleChange}
            className={inputClass}
          />
          <select
            name="staff_role"
            value={formData.staff_role}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="Teaching">Teaching</option>
            <option value="Non Teaching">Non Teaching</option>
            <option value="Admin">Admin</option>
            <option value="Support">Support</option>
          </select>
          <select
            name="employment_type"
            value={formData.employment_type}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="">Select Employment Type</option>
            <option value="Regular">Regular</option>
            <option value="Contract">Contract</option>
            <option value="Guest">Guest</option>
            <option value="Part Time">Part Time</option>
          </select>
          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            className={inputClass}
          >
            <option value="Active">Active</option>
            <option value="Transferred">Transferred</option>
            <option value="Retired">Retired</option>
            <option value="Resigned">Resigned</option>
            <option value="Suspended">Suspended</option>
            <option value="Long Leave">Long Leave</option>
          </select>
          
          <input
            name="qualification"
            placeholder="Qualification"
            value={formData.qualification}
            onChange={handleChange}
            className={inputClass}
          />
          
          <input
            type="number"
            name="priority"
            placeholder="Priority"
            value={formData.priority}
            onChange={handleChange}
            className={inputClass}
          />

          {/* Conditional Teaching Fields */}
          {formData.staff_role === "Teaching" && (
            <>
              <select
                name="subject"
                value={formData.subject}
                onChange={handleChange}
                className={inputClass}
              >
                <option value="">Select Subject</option>
                {subjects.map((item) => (
                  <option key={item.id} value={item.id}>
                    {item.name}
                  </option>
                ))}
              </select>

              <input
                type="number"
                step="0.5"
                name="teaching_experience_years"
                placeholder="Teaching Experience (Years)"
                value={formData.teaching_experience_years}
                onChange={handleChange}
                className={inputClass}
              />
              
              <input
                type="number"
                name="min_periods_per_week"
                placeholder="Min Periods / Week"
                value={formData.min_periods_per_week}
                onChange={handleChange}
                className={inputClass}
              />
              
              <input
                type="number"
                name="max_periods_per_week"
                placeholder="Max Periods / Week"
                value={formData.max_periods_per_week}
                onChange={handleChange}
                className={inputClass}
              />
            </>
          )}
        </div>
      </div>

      {/* ============================================
          CONTACT INFORMATION
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Contact Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <input
            type="tel"
            name="mobile_number"
            inputMode="numeric"
            pattern="[0-9]{10}"
            maxLength={10}
            placeholder="Mobile Number"
            value={formData.mobile_number}
            onChange={(e) =>
              handleChange({
                target: {
                  name: "mobile_number",
                  type: "text",
                  value: e.target.value.replace(/\D/g, ""),
                },
              })
            }
            className={inputClass}
          />
          
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            value={formData.email}
            onChange={handleChange}
            className={inputClass}
          />
          
          <input
            type="tel"
            name="aadhar_number"
            inputMode="numeric"
            pattern="[0-9]{12}"
            maxLength={12}
            placeholder="Aadhaar Number"
            value={formData.aadhar_number}
            onChange={(e) =>
              handleChange({
                target: {
                  name: "aadhar_number",
                  type: "text",
                  value: e.target.value.replace(/\D/g, ""),
                },
              })
            }
            className={inputClass}
          />
        </div>
      </div>

      {/* ============================================
          ADDRESS
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Address</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <textarea
            name="address"
            placeholder="Address"
            value={formData.address}
            onChange={handleChange}
            rows={4}
            className={inputClass}
          />
          <div className="space-y-6">
            <input
              name="city"
              placeholder="City"
              value={formData.city}
              onChange={handleChange}
              className={inputClass}
            />
            <input
              name="state"
              placeholder="State"
              value={formData.state}
              onChange={handleChange}
              className={inputClass}
            />
            <input
              name="pin_code"
              placeholder="PIN Code"
              value={formData.pin_code}
              onChange={handleChange}
              className={inputClass}
            />
          </div>
        </div>
      </div>

      {/* ============================================
          DATE INFORMATION
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Date Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div>
            <label className="text-sm text-gray-600 block mb-1">Date of Birth</label>
            <input
              type="date"
              name="date_of_birth"
              value={formData.date_of_birth}
              onChange={handleChange}
              className={inputClass}
            />
          </div>
          <div>
            <label className="text-sm text-gray-600 block mb-1">Joining Date</label>
            <input
              type="date"
              name="joining_date"
              value={formData.joining_date}
              onChange={handleChange}
              className={inputClass}
            />
          </div>
          <div>
            <label className="text-sm text-gray-600 block mb-1">Current Joining Date</label>
            <input
              type="date"
              name="current_joining_date"
              value={formData.current_joining_date}
              onChange={handleChange}
              className={inputClass}
            />
          </div>
          <div>
            <label className="text-sm text-gray-600 block mb-1">Retirement Date</label>
            <input
              type="date"
              name="retirement_date"
              value={formData.retirement_date}
              onChange={handleChange}
              className={inputClass}
            />
          </div>
        </div>
      </div>

      {/* ============================================
          OTHER INFORMATION
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Other Information</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <input
            name="category"
            placeholder="Category"
            value={formData.category}
            onChange={handleChange}
            className={inputClass}
          />
          <textarea
            name="bio"
            placeholder="Bio"
            rows={5}
            value={formData.bio}
            onChange={handleChange}
            className={inputClass}
          />
        </div>
      </div>

      {/* ============================================
          FLAGS / SETTINGS
      ============================================ */}
      <div>
        <h2 className="text-xl font-semibold mb-4">Additional Settings</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <label className="flex items-center gap-3 cursor-pointer select-none">
            <input
              type="checkbox"
              name="is_class_teacher"
              checked={formData.is_class_teacher}
              onChange={handleChange}
              className="w-5 h-5 cursor-pointer rounded border-gray-300 text-blue-600 focus:ring-blue-500"
            />
            <span>Class Teacher</span>
          </label>
          <label className="flex items-center gap-3 cursor-pointer select-none">
            <input
              type="checkbox"
              name="is_house_incharge"
              checked={formData.is_house_incharge}
              onChange={handleChange}
              className="w-5 h-5 cursor-pointer rounded border-gray-300 text-blue-600 focus:ring-blue-500"
            />
            <span>House Incharge</span>
          </label>
          <label className="flex items-center gap-3 cursor-pointer select-none">
            <input
              type="checkbox"
              name="is_active"
              checked={formData.is_active}
              onChange={handleChange}
              className="w-5 h-5 cursor-pointer rounded border-gray-300 text-blue-600 focus:ring-blue-500"
            />
            <span>Active</span>
          </label>
        </div>
      </div>

      {/* ============================================
          SUBMIT BUTTON
      ============================================ */}
      <div className="pt-6 border-t">
        <div className="flex justify-end">
          <button
            type="submit"
            disabled={loading}
            className="px-8 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold transition"
          >
            {loading ? "Saving Staff..." : "Save Staff"}
          </button>
        </div>
      </div>
    </form>
  );
};

export default StaffForm;