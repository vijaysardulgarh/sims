// ============================================
// POST TYPE FORM
// File: PostTypeForm.jsx
// ============================================

import {
  useEffect,
  useState,
} from "react";

const PostTypeForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // FORM STATE
  // ============================================

  const [formData, setFormData] =
    useState({

      name: "",

      description: "",
    });

  // ============================================
  // PREFILL
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        name:
          initialData.name || "",

        description:
          initialData.description || "",
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
  // HANDLE SUBMIT
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
        p-6
        rounded-2xl
        shadow
        space-y-6
      "
    >

      {/* POST TYPE NAME */}

      <div>

        <label
          className="
            block
            mb-2
            font-medium
          "
        >

          Post Type Name

        </label>

        <input

          type="text"

          name="name"

          value={formData.name}

          onChange={handleChange}

          placeholder="Enter post type"

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

      {/* DESCRIPTION */}

      <div>

        <label
          className="
            block
            mb-2
            font-medium
          "
        >

          Description

        </label>

        <textarea

          name="description"

          value={formData.description}

          onChange={handleChange}

          rows="4"

          placeholder="Enter description"

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
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

            : "Save Post Type"

        }

      </button>

    </form>

  );

};

export default PostTypeForm;