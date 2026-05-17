// ============================================
// STAFF FORM
// File: StaffForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import postTypeService from
"../post-types/postTypeService";

const StaffForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // STATES
  // ============================================

  const [postTypes,
    setPostTypes] =
    useState([]);

  const [formData, setFormData] =
    useState({

      first_name: "",

      last_name: "",

      email: "",

      mobile_number: "",

      employee_id: "",

      qualification: "",

      joining_date: "",

      post_type: "",
    });

  // ============================================
  // FETCH POST TYPES
  // ============================================

  useEffect(() => {

    fetchPostTypes();

  }, []);

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

  // ============================================
  // PREFILL
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        first_name:
          initialData.first_name || "",

        last_name:
          initialData.last_name || "",

        email:
          initialData.email || "",

        mobile_number:
          initialData.mobile_number || "",

        employee_id:
          initialData.employee_id || "",

        qualification:
          initialData.qualification || "",

        joining_date:
          initialData.joining_date || "",

        post_type:
          initialData.post_type || "",
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

      {/* FIRST NAME */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          First Name
        </label>

        <input

          type="text"

          name="first_name"

          value={formData.first_name}

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

      {/* LAST NAME */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Last Name
        </label>

        <input

          type="text"

          name="last_name"

          value={formData.last_name}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* EMAIL */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Email
        </label>

        <input

          type="email"

          name="email"

          value={formData.email}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* MOBILE */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Mobile Number
        </label>

        <input

          type="text"

          name="mobile_number"

          value={formData.mobile_number}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* EMPLOYEE ID */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Employee ID
        </label>

        <input

          type="text"

          name="employee_id"

          value={formData.employee_id}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* QUALIFICATION */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Qualification
        </label>

        <input

          type="text"

          name="qualification"

          value={formData.qualification}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* JOINING DATE */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Joining Date
        </label>

        <input

          type="date"

          name="joining_date"

          value={formData.joining_date}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* POST TYPE */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Post Type
        </label>

        <select

          name="post_type"

          value={formData.post_type}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        >

          <option value="">
            Select Post Type
          </option>

          {

            postTypes.map((item) => (

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

          : "Save Staff"}

      </button>

    </form>
  );
};

export default StaffForm;