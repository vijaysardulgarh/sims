import {
  useState,
  useEffect
} from "react";

const ClassroomForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  const [formData, setFormData] =
    useState({

      name: "",

      capacity: "",

      floor: "",

      description: "",
    });

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

        floor:
          initialData.floor || "",

        description:
          initialData.description || "",
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

    onSubmit({
      ...formData,
      capacity: Number(formData.capacity),
    });
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

      {/* CLASSROOM NAME */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >
          Classroom Name
        </label>

        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="e.g. Computer Lab"
          className="
            w-full
            border
            rounded-lg
            p-3
          "
          required
        />

      </div>

      {/* CAPACITY */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >
          Capacity
        </label>

        <input
          type="number"
          name="capacity"
          value={formData.capacity}
          onChange={handleChange}
          placeholder="Enter capacity"
          min="1"
          className="
            w-full
            border
            rounded-lg
            p-3
          "
        />

      </div>

      {/* FLOOR */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >
          Floor
        </label>

        <input
          type="text"
          name="floor"
          value={formData.floor}
          onChange={handleChange}
          placeholder="Ground Floor"
          className="
            w-full
            border
            rounded-lg
            p-3
          "
        />

      </div>

      {/* DESCRIPTION */}

      <div>

        <label
          className="
            block
            mb-2
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
          rows="4"
          placeholder="Optional description"
          className="
            w-full
            border
            rounded-lg
            p-3
          "
        />

      </div>

      {/* SUBMIT */}

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
          disabled:opacity-50
        "
      >

        {loading
          ? "Saving..."
          : "Save Classroom"}

      </button>

    </form>
  );
};

export default ClassroomForm;