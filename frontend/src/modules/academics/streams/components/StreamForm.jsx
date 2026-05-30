// ============================================
// STREAM FORM
// File: StreamForm.jsx
// ============================================

import {
  useState,
  useEffect
} from "react";

const StreamForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // STREAM OPTIONS
  // ============================================

  const streamOptions = [

    {
      name: "Science",
      code: "SCI"
    },

    {
      name: "Commerce",
      code: "COM"
    },

    {
      name: "Arts",
      code: "ART"
    },

    {
      name: "Medical",
      code: "MED"
    },

    {
      name: "Non Medical",
      code: "NMD"
    },
  ];

  // ============================================
  // FORM STATE
  // ============================================

  const [formData, setFormData] =
    useState({

      name: "",

      code: "",
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

        code:
          initialData.code || "",
      });
    }

  }, [initialData]);

  // ============================================
  // HANDLE STREAM CHANGE
  // ============================================

  const handleStreamChange = (e) => {

    const selectedStream =
      e.target.value;

    const selectedOption =
      streamOptions.find(
        (item) =>
          item.name === selectedStream
      );

    setFormData({

      ...formData,

      name: selectedStream,

      code:
        selectedOption?.code || "",
    });
  };

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

      {/* STREAM NAME */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Stream Name
        </label>

        <select

          name="name"

          value={formData.name}

          onChange={handleStreamChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required
        >

          <option value="">
            Select Stream
          </option>

          {

            streamOptions.map(
              (stream, index) => (

                <option
                  key={index}
                  value={stream.name}
                >

                  {stream.name}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* STREAM CODE */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Stream Code
        </label>

        <input

          type="text"

          name="code"

          value={formData.code}

          onChange={handleChange}

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
          : "Save Stream"}

      </button>

    </form>
  );
};

export default StreamForm;