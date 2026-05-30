import {
  useState,
  useEffect
} from "react";

const ClassForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // =========================
  // FORM STATE
  // =========================

  const [formData, setFormData] =
    useState({

      name: "",

      display_order: "",
    });

  // =========================
  // PREFILL FORM
  // =========================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        name:
          initialData.name || "",

        display_order:
          initialData.display_order || "",
      });
    }

  }, [initialData]);

  // =========================
  // HANDLE CHANGE
  // =========================

  const handleChange = (e) => {

    const { name, value } = e.target;

    setFormData({

      ...formData,

      [name]: value,
    });
  };

  // =========================
  // SUBMIT
  // =========================

  const handleSubmit = (e) => {

    e.preventDefault();

    onSubmit(formData);
  };

  return (

    <form
      onSubmit={handleSubmit}
      className="
        rounded-2xl
        bg-white
        p-6
        shadow
        space-y-6
      "
    >

      {/* ===================== */}
      {/* CLASS NAME */}
      {/* ===================== */}

      <div>

        <label className="
          mb-2
          block
          text-sm
          font-medium
        ">

          Class Name

        </label>

        <input

          type="text"

          name="name"

          value={formData.name}

          onChange={handleChange}

          placeholder="Enter class name"

          className="
            w-full
            rounded-lg
            border
            p-3
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
          "

          required
        />

      </div>

      {/* ===================== */}
      {/* DISPLAY ORDER */}
      {/* ===================== */}

      <div>

        <label className="
          mb-2
          block
          text-sm
          font-medium
        ">

          Display Order

        </label>

        <input

          type="number"

          name="display_order"

          value={formData.display_order}

          onChange={handleChange}

          placeholder="Enter display order"

          className="
            w-full
            rounded-lg
            border
            p-3
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
          "

          required
        />

      </div>

      {/* ===================== */}
      {/* BUTTON */}
      {/* ===================== */}

      <button

        type="submit"

        disabled={loading}

        className="
          rounded-xl
          bg-blue-600
          px-6
          py-3
          text-white
          hover:bg-blue-700
          disabled:opacity-50
        "
      >

        {loading

          ? "Saving..."

          : "Save Class"}

      </button>

    </form>
  );
};

export default ClassForm;