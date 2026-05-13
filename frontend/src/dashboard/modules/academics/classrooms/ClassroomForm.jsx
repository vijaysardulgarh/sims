// ============================================
// CLASSROOM FORM
// File: ClassroomForm.jsx
// ============================================

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

      room_number: "",

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

        room_number:
          initialData.room_number || "",

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

      {/* CLASSROOM NAME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Classroom Name
        </label>

        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Enter classroom name"
          className="
            w-full
            border
            rounded-lg
            p-3
          "
          required
        />

      </div>

      {/* ROOM NUMBER */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Room Number
        </label>

        <input
          type="text"
          name="room_number"
          value={formData.room_number}
          onChange={handleChange}
          placeholder="Enter room number"
          className="
            w-full
            border
            rounded-lg
            p-3
          "
        />

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
          placeholder="Enter classroom capacity"
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
          : "Save Classroom"}

      </button>

    </form>
  );
};

export default ClassroomForm;