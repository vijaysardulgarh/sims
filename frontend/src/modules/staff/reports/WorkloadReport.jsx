// ============================================
// WORKLOAD REPORT
// File: WorkloadReport.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import reportService
from "./reportService";

const WorkloadReport = () => {

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
        await reportService.getWorkloadReport();

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

        Loading workload report...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
      ">

        Workload Report

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
                Teacher
              </th>

              <th className="p-4 text-left">
                Subject
              </th>

              <th className="p-4 text-left">
                Total Periods
              </th>

              <th className="p-4 text-left">
                Weekly Load
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
                    {item.subject_name}
                  </td>

                  <td className="p-4">
                    {item.total_periods}
                  </td>

                  <td className="p-4">
                    {item.weekly_load}
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

export default WorkloadReport;