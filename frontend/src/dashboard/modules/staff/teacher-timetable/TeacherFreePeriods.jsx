// ============================================
// TEACHER FREE PERIODS
// File: TeacherFreePeriods.jsx
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

const TeacherFreePeriods = () => {

  // ============================================
  // PARAMS
  // ============================================

  const { staffId } = useParams();

  // ============================================
  // STATES
  // ============================================

  const [periods, setPeriods] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchPeriods();

  }, []);

  const fetchPeriods = async () => {

    try {

      const response =
        await teacherTimetableService.getTeacherFreePeriods(
          staffId
        );

      setPeriods(

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

  if (loading) {

    return (

      <div className="p-6">

        Loading free periods...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
        text-gray-800
      ">

        Teacher Free Periods

      </h1>

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
                Time
              </th>

            </tr>

          </thead>

          <tbody>

            {

              periods.map((item) => (

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
                    {item.time_range}
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

export default TeacherFreePeriods;