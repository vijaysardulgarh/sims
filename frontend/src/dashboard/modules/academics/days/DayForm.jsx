// ============================================
// DAY FORM
// File: DayForm.jsx
// ============================================

import {
  useState,
  useEffect
} from "react";

const DayForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // DAYS OPTIONS
  // ============================================

  const dayOptions = [

    { name: "Monday", order: 1 },

    { name: "Tuesday", order: 2 },

    { name: "Wednesday", order: 3 },

    { name: "Thursday", order: 4 },

    { name: "Friday", order: 5 },

    { name: "Saturday", order: 6 },

    { name: "Sunday", order: 7 },
  ];

  // ============================================
  // FORM STATE
  // ============================================

  const [formData, setFormData] =
    useState({

      name: "",

      day_order: "",
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

        day_order:
          initialData.day_order || "",
      });
    }

  }, [initialData]);

  // ============================================
  // HANDLE DAY CHANGE
  // ============================================

  const handleDayChange = (e) => {

    const selectedDay =
      e.target.value;

    const selectedOption =
      dayOptions.find(
        (item) =>
          item.name === selectedDay
      );

    setFormData({

      ...formData,

      name: selectedDay,

      day_order:
        selectedOption?.order || "",
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

      {/* DAY NAME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Day Name
        </label>

        <select

          name="name"

          value={formData.name}

          onChange={handleDayChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required
        >

          <option value="">
            Select Day
          </option>

          {

            dayOptions.map(
              (day, index) => (

                <option
                  key={index}
                  value={day.name}
                >

                  {day.name}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* DAY ORDER */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Day Order
        </label>

        <input

          type="number"

          name="day_order"

          value={formData.day_order}

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
          : "Save Day"}

      </button>

    </form>
  );
};

export default DayForm;