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

      class_order: "",
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

        class_order:
          initialData.class_order || "",
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
      {/* CLASS ORDER */}
      {/* ===================== */}

      <div>

        <label className="
          mb-2
          block
          text-sm
          font-medium
        ">

          Class Order

        </label>

        <input

          type="number"

          name="class_order"

          value={formData.class_order}

          onChange={handleChange}

          placeholder="Enter class order"

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