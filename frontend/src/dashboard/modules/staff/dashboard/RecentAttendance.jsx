// ============================================
// RECENT ATTENDANCE
// File: RecentAttendance.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import dashboardService
from "./dashboardService";

const RecentAttendance = () => {

  // ============================================
  // STATES
  // ============================================

  const [attendance,
    setAttendance] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchAttendance();

  }, []);

  const fetchAttendance = async () => {

    try {

      const response =
        await dashboardService.getRecentAttendance();

      setAttendance(

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

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        Loading attendance...

      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="
      bg-white
      rounded-2xl
      shadow
      overflow-hidden
    ">

      {/* HEADER */}

      <div className="
        p-6
        border-b
      ">

        <h2 className="
          text-2xl
          font-bold
          text-gray-800
        ">

          Recent Attendance

        </h2>

      </div>

      {/* TABLE */}

      <table className="w-full">

        <thead className="bg-gray-100">

          <tr>

            <th className="p-4 text-left">
              Staff
            </th>

            <th className="p-4 text-left">
              Date
            </th>

            <th className="p-4 text-left">
              Status
            </th>

          </tr>

        </thead>

        <tbody>

          {

            attendance.map((item) => (

              <tr
                key={item.id}
                className="border-t"
              >

                <td className="p-4">
                  {item.staff_name}
                </td>

                <td className="p-4">
                  {item.attendance_date}
                </td>

                <td className="p-4">

                  <span
                    className={`
                      px-3
                      py-1
                      rounded-full
                      text-sm
                      ${
                        item.status === "Present"

                          ? "bg-green-100 text-green-700"

                          : item.status === "Absent"

                          ? "bg-red-100 text-red-700"

                          : "bg-yellow-100 text-yellow-700"
                      }
                    `}
                  >

                    {item.status}

                  </span>

                </td>

              </tr>
            ))
          }

        </tbody>

      </table>

    </div>
  );
};

export default RecentAttendance;