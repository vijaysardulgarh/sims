// ============================================
// TIMETABLE FORM
// File: TimetableForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import classService from
"../../../services/academics/classService";

import sectionService from
"../../../services/academics/sectionService";

import subjectService from
"../../../services/academics/subjectService";

import staffService from
"../../../services/staff/staffService";

import dayService from
"../../../services/academics/dayService";

import classroomService from
"../../../services/academics/classroomService";

const TimetableForm = ({

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

      section: "",

      subject: "",

      teacher: "",

      day: "",

      classroom: "",

      start_time: "",

      end_time: "",
    });

  // ============================================
  // DROPDOWN DATA
  // ============================================

  const [classes, setClasses] =
    useState([]);

  const [sections, setSections] =
    useState([]);

  const [subjects, setSubjects] =
    useState([]);

  const [teachers, setTeachers] =
    useState([]);

  const [days, setDays] =
    useState([]);

  const [classrooms, setClassrooms] =
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

        classRes,

        sectionRes,

        subjectRes,

        teacherRes,

        dayRes,

        classroomRes,

      ] = await Promise.all([

        classService.getClasses(),

        sectionService.getSections(),

        subjectService.getSubjects(),

        staffService.getTeachers(),

        dayService.getDays(),

        classroomService.getClassrooms(),
      ]);

      setClasses(
        Array.isArray(classRes)
          ? classRes
          : classRes.results || []
      );

      setSections(
        Array.isArray(sectionRes)
          ? sectionRes
          : sectionRes.results || []
      );

      setSubjects(
        Array.isArray(subjectRes)
          ? subjectRes
          : subjectRes.results || []
      );

      setTeachers(
        Array.isArray(teacherRes)
          ? teacherRes
          : teacherRes.results || []
      );

      setDays(
        Array.isArray(dayRes)
          ? dayRes
          : dayRes.results || []
      );

      setClassrooms(
        Array.isArray(classroomRes)
          ? classroomRes
          : classroomRes.results || []
      );

    } catch (error) {

      console.log(error);
    }
  };

  // ============================================
  // PREFILL DATA
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        student_class:
          initialData.student_class || "",

        section:
          initialData.section || "",

        subject:
          initialData.subject || "",

        teacher:
          initialData.teacher || "",

        day:
          initialData.day || "",

        classroom:
          initialData.classroom || "",

        start_time:
          initialData.start_time || "",

        end_time:
          initialData.end_time || "",
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

      {/* CLASS */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          Class
        </label>

        <select
          name="student_class"
          value={formData.student_class}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
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

      {/* SECTION */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          Section
        </label>

        <select
          name="section"
          value={formData.section}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        >

          <option value="">
            Select Section
          </option>

          {

            sections.map((section) => (

              <option
                key={section.id}
                value={section.id}
              >

                {section.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* SUBJECT */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          Subject
        </label>

        <select
          name="subject"
          value={formData.subject}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
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

      {/* TEACHER */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          Teacher
        </label>

        <select
          name="teacher"
          value={formData.teacher}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        >

          <option value="">
            Select Teacher
          </option>

          {

            teachers.map((teacher) => (

              <option
                key={teacher.id}
                value={teacher.id}
              >

                {teacher.full_name}

              </option>
            ))
          }

        </select>

      </div>

      {/* DAY */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          Day
        </label>

        <select
          name="day"
          value={formData.day}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        >

          <option value="">
            Select Day
          </option>

          {

            days.map((day) => (

              <option
                key={day.id}
                value={day.id}
              >

                {day.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* CLASSROOM */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          Classroom
        </label>

        <select
          name="classroom"
          value={formData.classroom}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        >

          <option value="">
            Select Classroom
          </option>

          {

            classrooms.map((room) => (

              <option
                key={room.id}
                value={room.id}
              >

                {room.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* START TIME */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          Start Time
        </label>

        <input
          type="time"
          name="start_time"
          value={formData.start_time}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        />

      </div>

      {/* END TIME */}

      <div>

        <label className="block mb-2 text-sm font-medium">
          End Time
        </label>

        <input
          type="time"
          name="end_time"
          value={formData.end_time}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
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
        "
      >

        {loading
          ? "Saving..."
          : "Save Timetable"}

      </button>

    </form>
  );
};

export default TimetableForm;