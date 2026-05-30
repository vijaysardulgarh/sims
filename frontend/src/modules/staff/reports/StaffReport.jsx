// ============================================
// STAFF REPORT
// File: StaffReport.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import reportService
from "./reportService";

const StaffReport = () => {

  const [data, setData] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchReport();

  }, []);

  const fetchReport = async () => {

    try {

      const response =
        await reportService.getStaffReport();

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

        Loading report...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
      ">

        Staff Report

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
                Employee ID
              </th>

              <th className="p-4 text-left">
                Name
              </th>

              <th className="p-4 text-left">
                Post Type
              </th>

              <th className="p-4 text-left">
                Qualification
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
                    {item.employee_id}
                  </td>

                  <td className="p-4">
                    {item.full_name}
                  </td>

                  <td className="p-4">
                    {item.post_type_name}
                  </td>

                  <td className="p-4">
                    {item.qualification}
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

export default StaffReport;