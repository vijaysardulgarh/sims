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
  // EDIT MODE
  // =========================

  const isEdit =
    Boolean(initialData?.id);

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
          initialData.display_order ?? "",
      });
    }

  }, [initialData]);

  // =========================
  // HANDLE CHANGE
  // =========================

  const handleChange = (e) => {

    const {
      name,
      value
    } = e.target;

    setFormData((prev) => ({

      ...prev,

      [name]: value,
    }));
  };

  // =========================
  // SUBMIT
  // =========================

  const handleSubmit = (e) => {

    e.preventDefault();

    const payload = {

      ...formData,
    };

    if (
      payload.display_order === ""
    ) {

      delete payload.display_order;
    }

    onSubmit(payload);
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

        <label
          className="
            mb-2
            block
            text-sm
            font-medium
          "
        >

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
      {/* EDIT ONLY */}
      {/* ===================== */}

      {isEdit && (

        <div>

          <label
            className="
              mb-2
              block
              text-sm
              font-medium
            "
          >

            Display Order

          </label>

          <input

            type="number"

            name="display_order"

            value={formData.display_order}

            onChange={handleChange}

            placeholder="Enter display order"

            min="0"

            className="
              w-full
              rounded-lg
              border
              p-3
              focus:outline-none
              focus:ring-2
              focus:ring-blue-500
            "
          />

        </div>

      )}

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
          : isEdit
            ? "Update Class"
            : "Save Class"}

      </button>

    </form>
  );
};

export default ClassForm;