// ============================================
// MEDIUM FORM
// File: MediumForm.jsx
// ============================================

import {
  useState,
  useEffect
} from "react";

const MediumForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // MEDIUM OPTIONS
  // ============================================

  const mediumOptions = [

    "English",

    "Hindi",

    "Punjabi",

    "Sanskrit",

    "Urdu",
  ];

  // ============================================
  // FORM STATE
  // ============================================

  const [formData, setFormData] =
    useState({

      name: "",

      code: "",
    });

  // ============================================
  // PREFILL FORM
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        name:
          initialData.name || "",

        code:
          initialData.code || "",
      });
    }

  }, [initialData]);

  // ============================================
  // HANDLE MEDIUM CHANGE
  // ============================================

  const handleMediumChange = (e) => {

    const selectedMedium =
      e.target.value;

    setFormData({

      ...formData,

      name: selectedMedium,

      code:
        selectedMedium
          .substring(0, 3)
          .toUpperCase(),
    });
  };

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

      {/* MEDIUM NAME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Medium Name
        </label>

        <select

          name="name"

          value={formData.name}

          onChange={handleMediumChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required
        >

          <option value="">
            Select Medium
          </option>

          {

            mediumOptions.map(
              (medium, index) => (

                <option
                  key={index}
                  value={medium}
                >

                  {medium}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* MEDIUM CODE */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Medium Code
        </label>

        <input

          type="text"

          name="code"

          value={formData.code}

          onChange={handleChange}

          readOnly

          className="
            w-full
            border
            rounded-lg
            p-3
            bg-gray-100
          "
        />

      </div>

      {/* BUTTON */}

      <button

        type="submit"

        disabled={loading}

        className="
          bg-blue-600
          text-white
          px-6
          py-3
          rounded-xl
          hover:bg-blue-700
        "
      >

        {loading
          ? "Saving..."
          : "Save Medium"}

      </button>

    </form>
  );
};

export default MediumForm;