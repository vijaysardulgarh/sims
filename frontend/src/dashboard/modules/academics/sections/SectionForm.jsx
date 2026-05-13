// ============================================
// SECTION FORM
// File: SectionForm.jsx
// ============================================

import {
  useState,
  useEffect
} from "react";

const SectionForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // SECTION OPTIONS
  // ============================================

  const sectionOptions = [

    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
  ];

  // ============================================
  // FORM STATE
  // ============================================

  const [formData, setFormData] =
    useState({

      name: "",

      capacity: "",
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

        capacity:
          initialData.capacity || "",
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

      {/* SECTION NAME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Section Name
        </label>

        <select

          name="name"

          value={formData.name}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required
        >

          <option value="">
            Select Section
          </option>

          {

            sectionOptions.map(
              (section, index) => (

                <option
                  key={index}
                  value={section}
                >

                  {section}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* CAPACITY */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Capacity
        </label>

        <input

          type="number"

          name="capacity"

          value={formData.capacity}

          onChange={handleChange}

          placeholder="Enter section capacity"

          className="
            w-full
            border
            rounded-lg
            p-3
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
          : "Save Section"}

      </button>

    </form>
  );
};

export default SectionForm;