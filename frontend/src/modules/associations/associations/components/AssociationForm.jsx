import {
  useState,
  useEffect
} from "react";

const AssociationForm = ({

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

      association_type: "Club",

      status: "Active",

      description: "",

      tasks: "",

      priority: 0,

      show_on_website: true,
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

        association_type:
          initialData.association_type || "Club",

        status:
          initialData.status || "Active",

        description:
          initialData.description || "",

        tasks:
          initialData.tasks || "",

        priority:
          initialData.priority ?? 0,

        show_on_website:
          initialData.show_on_website ?? true,
      });
    }

  }, [initialData]);

  // =========================
  // HANDLE CHANGE
  // =========================

  const handleChange = (e) => {

    const {
      name,
      value,
      checked,
      type,
    } = e.target;

    setFormData((prev) => ({

      ...prev,

      [name]:

        type === "checkbox"

          ? checked

          : name === "priority"

            ? Number(value)

            : value,
    }));
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
      {/* NAME */}
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

          Association Name

        </label>

        <input

          type="text"

          name="name"

          value={formData.name}

          onChange={handleChange}

          placeholder="Enter association name"

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
      {/* TYPE */}
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

          Association Type

        </label>

        <select

          name="association_type"

          value={formData.association_type}

          onChange={handleChange}

          className="
            w-full
            rounded-lg
            border
            p-3
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
          "
        >

          <option value="Club">
            Club
          </option>

          <option value="Committee">
            Committee
          </option>

          <option value="Nodal">
            Nodal
          </option>

        </select>

      </div>

      {/* ===================== */}
      {/* STATUS */}
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

          Status

        </label>

        <select

          name="status"

          value={formData.status}

          onChange={handleChange}

          className="
            w-full
            rounded-lg
            border
            p-3
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
          "
        >

          <option value="Active">
            Active
          </option>

          <option value="Inactive">
            Inactive
          </option>

          <option value="Archived">
            Archived
          </option>

        </select>

      </div>

      {/* ===================== */}
      {/* DESCRIPTION */}
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

          Description

        </label>

        <textarea

          name="description"

          value={formData.description}

          onChange={handleChange}

          rows={4}

          placeholder="Enter description"

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

      {/* ===================== */}
      {/* TASKS */}
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

          Tasks

        </label>

        <textarea

          name="tasks"

          value={formData.tasks}

          onChange={handleChange}

          rows={4}

          placeholder="Enter tasks"

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

      {/* ===================== */}
      {/* PRIORITY */}
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

          Priority

        </label>

        <input

          type="number"

          name="priority"

          value={formData.priority}

          onChange={handleChange}

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

      {/* ===================== */}
      {/* SHOW ON WEBSITE */}
      {/* ===================== */}

      <div
        className="
          flex
          items-center
          gap-3
        "
      >

        <input

          type="checkbox"

          name="show_on_website"

          checked={formData.show_on_website}

          onChange={handleChange}
        />

        <label>

          Show On Website

        </label>

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

        {
          loading

            ? "Saving..."

            : isEdit

              ? "Update Association"

              : "Save Association"
        }

      </button>

    </form>
  );
};

export default AssociationForm;