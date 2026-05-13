// ============================================
// TIMETABLE SLOT FORM
// File: TimetableSlotForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

const TimetableSlotForm = ({

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

      start_time: "",

      end_time: "",

      slot_order: "",
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

        start_time:
          initialData.start_time || "",

        end_time:
          initialData.end_time || "",

        slot_order:
          initialData.slot_order || "",
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

      {/* SLOT NAME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Slot Name
        </label>

        <input

          type="text"

          name="name"

          value={formData.name}

          onChange={handleChange}

          placeholder="Example: Period 1"

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required
        />

      </div>

      {/* START TIME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Start Time
        </label>

        <input

          type="time"

          name="start_time"

          value={formData.start_time}

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

      {/* END TIME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          End Time
        </label>

        <input

          type="time"

          name="end_time"

          value={formData.end_time}

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

      {/* SLOT ORDER */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Slot Order
        </label>

        <input

          type="number"

          name="slot_order"

          value={formData.slot_order}

          onChange={handleChange}

          placeholder="Enter slot order"

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required
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
          : "Save Slot"}

      </button>

    </form>
  );
};

export default TimetableSlotForm;