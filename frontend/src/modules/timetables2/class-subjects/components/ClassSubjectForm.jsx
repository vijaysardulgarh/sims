// ============================================
// CLASS SUBJECT FORM
// File: ClassSubjectForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

// import classService from
// "../../../services/academics/classService";

// import subjectService from
// "../../../services/academics/subjectService";

// import streamService from
// "../../../services/academics/streamService";


import classService from "../../classes/services/classService";
import subjectService from "../../subjects/services/subjectService";
import streamService from "../../streams/services/streamService";

const ClassSubjectForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // FORM STATE
  // ============================================

  const [formData, setFormData] =
    useState({

      student_class: "",

      subject: "",

      stream: "",

      is_optional: false,
    });

  // ============================================
  // DROPDOWNS
  // ============================================

  const [classes, setClasses] =
    useState([]);

  const [subjects, setSubjects] =
    useState([]);

  const [streams, setStreams] =
    useState([]);

  // ============================================
  // FETCH DROPDOWNS
  // ============================================

  useEffect(() => {

    fetchDropdowns();

  }, []);

  const fetchDropdowns = async () => {

    try {

      const [

        classResponse,

        subjectResponse,

        streamResponse,

      ] = await Promise.all([

        classService.getClasses(),

        subjectService.getSubjects(),

        streamService.getStreams(),
      ]);

      setClasses(

        Array.isArray(classResponse)

          ? classResponse

          : classResponse.results || []
      );

      setSubjects(

        Array.isArray(subjectResponse)

          ? subjectResponse

          : subjectResponse.results || []
      );

      setStreams(

        Array.isArray(streamResponse)

          ? streamResponse

          : streamResponse.results || []
      );

    } catch (error) {

      console.log(error);
    }
  };

  // ============================================
  // PREFILL FORM
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        student_class:
          initialData.student_class || "",

        subject:
          initialData.subject || "",

        stream:
          initialData.stream || "",

        is_optional:
          initialData.is_optional || false,
      });
    }

  }, [initialData]);

  // ============================================
  // HANDLE CHANGE
  // ============================================

  const handleChange = (e) => {

    const {

      name,

      value,

      type,

      checked

    } = e.target;

    setFormData({

      ...formData,

      [name]:

        type === "checkbox"

          ? checked

          : value,
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

      {/* CLASS */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Class
        </label>

        <select

          name="student_class"

          value={formData.student_class}

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

            classes.map((cls) => (

              <option
                key={cls.id}
                value={cls.id}
              >

                {cls.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* SUBJECT */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
          Subject
        </label>

        <select

          name="subject"

          value={formData.subject}

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
            Select Subject
          </option>

          {

            subjects.map((subject) => (

              <option
                key={subject.id}
                value={subject.id}
              >

                {subject.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* STREAM */}

      <div>

        <label className="
          block
          mb-2
          text-sm
          font-medium
        ">
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

            streams.map((stream) => (

              <option
                key={stream.id}
                value={stream.id}
              >

                {stream.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* OPTIONAL SUBJECT */}

      <div className="
        flex
        items-center
        gap-3
      ">

        <input

          type="checkbox"

          name="is_optional"

          checked={formData.is_optional}

          onChange={handleChange}

          className="
            h-5
            w-5
          "
        />

        <label className="
          text-sm
          font-medium
        ">
          Optional Subject
        </label>

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
          : "Save Class Subject"}

      </button>

    </form>
  );
};

export default ClassSubjectForm;