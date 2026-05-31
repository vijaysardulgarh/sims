// ============================================
// SECTION FORM
// File: SectionForm.jsx
// ============================================

import {
  useState,
  useEffect
} from "react";

const SectionForm = ({

  initialData = {},

  classes = [],

  mediums = [],

  streams = [],

  classrooms = [],

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // OPTIONS
  // ============================================

  const sectionOptions = [

    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
  ];

  const subStreamOptions = [

    "Medical",

    "Non-Medical",

    "Vocational",
  ];

  // ============================================
  // FORM STATE
  // ============================================

  const [formData, setFormData] =
    useState({

      class_obj: "",

      name: "",

      medium: "",

      stream: "",

      sub_stream: "",

      classroom: "",
    });

  // ============================================
  // PREFILL
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        class_obj:
          initialData.class_obj
            ? String(
                initialData.class_obj
              )
            : "",

        name:
          initialData.name || "",

        medium:
          initialData.medium
            ? String(
                initialData.medium
              )
            : "",

        stream:
          initialData.stream
            ? String(
                initialData.stream
              )
            : "",

        sub_stream:
          initialData.sub_stream || "",

        classroom:
          initialData.classroom
            ? String(
                initialData.classroom
              )
            : "",
      });
    }

  }, [initialData]);

  // ============================================
  // HANDLE CHANGE
  // ============================================

  const handleChange = (e) => {

    const {
      name,
      value
    } = e.target;

    setFormData({

      ...formData,

      [name]: value,
    });
  };

  // ============================================
  // SUBMIT
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

      {/* CLASS */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Class

        </label>

        <select

          name="class_obj"

          value={formData.class_obj}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required
        >

          <option value="">
            Select Class
          </option>

          {

            classes.map(
              (cls) => (

                <option
                  key={cls.id}
                  value={String(cls.id)}
                >

                  {cls.name}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* SECTION */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Section

        </label>

        <select

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
        >

          <option value="">
            Select Section
          </option>

          {

            sectionOptions.map(
              (section) => (

                <option
                  key={section}
                  value={section}
                >

                  {section}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* MEDIUM */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Medium

        </label>

        <select

          name="medium"

          value={formData.medium}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "
        >

          <option value="">
            Select Medium
          </option>

          {

            mediums.map(
              (medium) => (

                <option
                  key={medium.id}
                  value={String(
                    medium.id
                  )}
                >

                  {medium.name}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* STREAM */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Stream

        </label>

        <select

          name="stream"

          value={formData.stream}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "
        >

          <option value="">
            Select Stream
          </option>

          {

            streams.map(
              (stream) => (

                <option
                  key={stream.id}
                  value={String(
                    stream.id
                  )}
                >

                  {stream.name}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* SUB STREAM */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Sub Stream

        </label>

        <select

          name="sub_stream"

          value={formData.sub_stream}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "
        >

          <option value="">
            Select Sub Stream
          </option>

          {

            subStreamOptions.map(
              (item) => (

                <option
                  key={item}
                  value={item}
                >

                  {item}

                </option>
              )
            )
          }

        </select>

      </div>

      {/* CLASSROOM */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Classroom

        </label>

        <select

          name="classroom"

          value={formData.classroom}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "
        >

          <option value="">
            Select Classroom
          </option>

          {

            classrooms.map(
              (classroom) => (

                <option
                  key={classroom.id}
                  value={String(
                    classroom.id
                  )}
                >

                  {classroom.name}

                </option>
              )
            )
          }

        </select>

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
          disabled:opacity-50
        "
      >

        {

          loading

            ? "Saving..."

            : "Save Section"
        }

      </button>

    </form>
  );
};

export default SectionForm;