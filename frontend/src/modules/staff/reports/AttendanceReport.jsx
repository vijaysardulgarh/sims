// ============================================
// ATTENDANCE REPORT
// File: AttendanceReport.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import reportService
from "./reportService";

const AttendanceReport = () => {

  const [data, setData] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    fetchReport();

  }, []);

  const fetchReport = async () => {

    try {

      const response =
        await reportService.getAttendanceReport();

      setData(

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

        Loading attendance report...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
      ">

        Attendance Report

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
                Staff
              </th>

              <th className="p-4 text-left">
                Date
              </th>

              <th className="p-4 text-left">
                Status
              </th>

              <th className="p-4 text-left">
                Remarks
              </th>

            </tr>

          </thead>

          <tbody>

            {

              data.map((item) => (

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
                    {item.status}
                  </td>

                  <td className="p-4">
                    {item.remarks}
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

export default AttendanceReport;