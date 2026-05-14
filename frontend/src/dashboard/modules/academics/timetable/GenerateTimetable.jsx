// ============================================
// GENERATE TIMETABLE
// File: GenerateTimetable.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import toast from "react-hot-toast";

import classService from
"../../../services/academics/classService";

import sectionService from
"../../../services/academics/sectionService";

import timetableService from "./timetableService";



const GenerateTimetable = () => {

  // ============================================
  // STATES
  // ============================================

  const [loading, setLoading] =
    useState(false);

  const [classes, setClasses] =
    useState([]);

  const [sections, setSections] =
    useState([]);

  const [filteredSections,
    setFilteredSections] =
    useState([]);

  const [formData, setFormData] =
    useState({

      student_class: "",

      section: "",

      total_periods: 8,

      start_time: "08:00",

      period_duration: 45,
    });

  // ============================================
  // FETCH DATA
  // ============================================

  useEffect(() => {

    fetchDropdowns();

  }, []);

  const fetchDropdowns = async () => {

    try {

      const [

        classResponse,

        sectionResponse,

      ] = await Promise.all([

        classService.getClasses(),

        sectionService.getSections(),
      ]);

      setClasses(

        Array.isArray(classResponse)

          ? classResponse

          : classResponse.results || []
      );

      const sectionData =

        Array.isArray(sectionResponse)

          ? sectionResponse

          : sectionResponse.results || [];

      setSections(sectionData);

    } catch (error) {

      console.log(error);

      toast.error(
        "Failed to load data"
      );
    }
  };

  // ============================================
  // FILTER SECTIONS
  // ============================================

  useEffect(() => {

    if (!formData.student_class) {

      setFilteredSections([]);

      return;
    }

    const filtered = sections.filter(
      (section) =>

        String(

          section.student_class ||

          section.student_class_data?.id ||

          section.class_id

        ) ===
        
        String(formData.student_class)
    );

    setFilteredSections(filtered);

  }, [

    formData.student_class,

    sections
  ]);

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
  // GENERATE TIMETABLE
  // ============================================

  const handleGenerate = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      await timetableService.generateTimetable(

        formData
      );

      toast.success(
        "Timetable generated successfully"
      );

    } catch (error) {

      console.log(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Failed to generate timetable"
      );

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="space-y-6">

      {/* PAGE HEADER */}

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">
          Generate Timetable
        </h1>

        <p className="
          text-gray-500
          mt-1
        ">
          Auto generate timetable for classes
        </p>

      </div>

      {/* FORM */}

      <form

        onSubmit={handleGenerate}

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

        {/* SECTION */}

        <div>

          <label className="
            block
            mb-2
            text-sm
            font-medium
          ">
            Section
          </label>

          <select

            name="section"

            value={formData.section}

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

              filteredSections.map((section) => (

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

        {/* TOTAL PERIODS */}

        <div>

          <label className="
            block
            mb-2
            text-sm
            font-medium
          ">
            Total Periods
          </label>

          <input

            type="number"

            name="total_periods"

            value={formData.total_periods}

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

        {/* PERIOD DURATION */}

        <div>

          <label className="
            block
            mb-2
            text-sm
            font-medium
          ">
            Period Duration (Minutes)
          </label>

          <input

            type="number"

            name="period_duration"

            value={formData.period_duration}

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

          {loading

            ? "Generating..."

            : "Generate Timetable"}

        </button>

      </form>

    </div>
  );
};

export default GenerateTimetable;