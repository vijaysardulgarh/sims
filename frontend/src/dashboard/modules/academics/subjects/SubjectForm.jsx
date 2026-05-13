// ============================================
// SUBJECT FORM
// File: SubjectForm.jsx
// ============================================

import {
  useState,
  useEffect
} from "react";

const SubjectForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  const [formData, setFormData] =
    useState({

      name: "",

      code: "",
    });

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

  const handleChange = (e) => {

    const { name, value } = e.target;

    setFormData({

      ...formData,

      [name]: value,
    });
  };

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

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Subject Name
        </label>

        <input
          type="text"
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
        />

      </div>

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Subject Code
        </label>

        <input
          type="text"
          name="code"
          value={formData.code}
          onChange={handleChange}
          className="
            w-full
            border
            rounded-lg
            p-3
          "
        />

      </div>

      <button
        type="submit"
        disabled={loading}
        className="
          bg-blue-600
          text-white
          px-6
          py-3
          rounded-xl
        "
      >

        {loading
          ? "Saving..."
          : "Save Subject"}

      </button>

    </form>
  );
};

export default SubjectForm;