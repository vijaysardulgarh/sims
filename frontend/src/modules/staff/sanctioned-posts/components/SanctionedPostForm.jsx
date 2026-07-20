// ============================================
// SANCTIONED POST FORM
// File: SanctionedPostForm.jsx
// ============================================

import {
  useEffect,
  useState,
} from "react";

import postTypeService from "../../post-types/services/postTypeService";

const SanctionedPostForm = ({

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

  const [formData,
    setFormData] =
    useState({

      post_type: "",

      sanctioned_posts: "",

      regular_working: "",

      guest_working: "",

      hkrnl_working: "",
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

      console.error(error);

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

        post_type:
          initialData.post_type || "",

        sanctioned_posts:
          initialData.sanctioned_posts || "",

        regular_working:
          initialData.regular_working || "",

        guest_working:
          initialData.guest_working || "",

        hkrnl_working:
          initialData.hkrnl_working || "",

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
  // CALCULATIONS
  // ============================================

  const sanctioned =
    Number(formData.sanctioned_posts) || 0;

  const regular =
    Number(formData.regular_working) || 0;

  const guest =
    Number(formData.guest_working) || 0;

  const hkrnl =
    Number(formData.hkrnl_working) || 0;

  const regularVacancy =
    Math.max(
      0,
      sanctioned - regular
    );

  const netVacancy =
    Math.max(
      0,
      sanctioned -
      regular -
      guest -
      hkrnl
    );

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

          required
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

      {/* SANCTIONED POSTS */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Sanctioned Posts
        </label>

        <input

          type="number"

          name="sanctioned_posts"

          value={formData.sanctioned_posts}

          onChange={handleChange}

          min="0"

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

      {/* REGULAR WORKING */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Regular Working
        </label>

        <input

          type="number"

          name="regular_working"

          value={formData.regular_working}

          onChange={handleChange}

          min="0"

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

      {/* REGULAR VACANCY */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Regular Vacancy
        </label>

        <input

          type="number"

          value={regularVacancy}

          readOnly

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
            bg-gray-100
            cursor-not-allowed
          "
        />

      </div>

      {/* GUEST WORKING */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Guest Working
        </label>

        <input

          type="number"

          name="guest_working"

          value={formData.guest_working}

          onChange={handleChange}

          min="0"

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* HKRNL WORKING */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          HKRNL Working
        </label>

        <input

          type="number"

          name="hkrnl_working"

          value={formData.hkrnl_working}

          onChange={handleChange}

          min="0"

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* NET VACANCY */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Net Vacancy
        </label>

        <input

          type="number"

          value={netVacancy}

          readOnly

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
            bg-gray-100
            cursor-not-allowed
          "
        />

      </div>

      {/* SAVE BUTTON */}

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
          disabled:opacity-50
        "
      >

        {

          loading

            ? "Saving..."

            : "Save Sanctioned Post"

        }

      </button>

    </form>

  );

};

export default SanctionedPostForm;