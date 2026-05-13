// ============================================
// TEACHER TIMETABLE
// File: TeacherTimetable.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useParams
} from "react-router-dom";

import teacherTimetableService
from "./teacherTimetableService";

const TeacherTimetable = () => {

  // ============================================
  // PARAMS
  // ============================================

  const { staffId } = useParams();

  // ============================================
  // STATES
  // ============================================

  const [timetable, setTimetable] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchTimetable();

  }, []);

  const fetchTimetable = async () => {

    try {

      const response =
        await teacherTimetableService.getTeacherTimetable(
          staffId
        );

      setTimetable(

        Array.isArray(response)

          ? response

          : response.results || []
      );

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  // ============================================
  // LOADING
  // ============================================

  if (loading) {

    return (

      <div className="p-6">

        Loading timetable...

      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">

          Teacher Timetable

        </h1>

      </div>

      <div className="
        bg-white
        rounded-2xl
        shadow
        overflow-hidden
      ">

        <table className="w-full">

          <thead className="bg-gray-100">

            <tr>

              <th className="p-4 text-left">
                Day
              </th>

              <th className="p-4 text-left">
                Period
              </th>

              <th className="p-4 text-left">
                Class
              </th>

              <th className="p-4 text-left">
                Section
              </th>

              <th className="p-4 text-left">
                Subject
              </th>

              <th className="p-4 text-left">
                Room
              </th>

            </tr>

          </thead>

          <tbody>

            {

              timetable.map((item) => (

                <tr
                  key={item.id}
                  className="border-t"
                >

                  <td className="p-4">
                    {item.day_name}
                  </td>

                  <td className="p-4">
                    {item.slot_name}
                  </td>

                  <td className="p-4">
                    {item.class_name}
                  </td>

                  <td className="p-4">
                    {item.section_name}
                  </td>

                  <td className="p-4">
                    {item.subject_name}
                  </td>

                  <td className="p-4">
                    {item.classroom_name}
                  </td>

                </tr>
              ))
            }

          </tbody>

        </table>

      </div>

    </div>
  );
};

export default TeacherTimetable;