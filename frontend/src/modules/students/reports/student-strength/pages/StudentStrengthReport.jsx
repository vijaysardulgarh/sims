import {
  useEffect,
  useState,
} from "react";

import studentStrengthService
from "../services/studentStrengthService";

const StudentStrengthReport = () => {

  const [rows, setRows] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    const fetchReport =
      async () => {

        try {

          const data =

            await studentStrengthService
              .getStudentStrength();

          setRows(data);

        } catch (error) {

          console.error(
            "Failed to load report",
            error
          );

        } finally {

          setLoading(false);
        }

      };

    fetchReport();

  }, []);

  const handlePrint = () => {

    window.print();

  };

const handleExcelDownload = async () => {

  try {

    const response =

      await studentStrengthService
        .downloadExcel();

    const url =

      window.URL.createObjectURL(

        new Blob(
          [response.data]
        )

      );

    const link =

      document.createElement(
        "a"
      );

    link.href = url;

    link.setAttribute(

      "download",

      "student_strength.xlsx"

    );

    document.body.appendChild(
      link
    );

    link.click();

    link.remove();

    window.URL.revokeObjectURL(
      url
    );

  } catch (error) {

    console.error(
      "Excel download failed",
      error
    );

  }

};

const handlePdfDownload = async () => {

  try {

    const response =

      await studentStrengthService
        .downloadPdf();

    const url =

      window.URL.createObjectURL(

        new Blob(
          [response.data]
        )

      );

    const link =

      document.createElement(
        "a"
      );

    link.href = url;

    link.setAttribute(

      "download",

      "student_strength.pdf"

    );

    document.body.appendChild(
      link
    );

    link.click();

    link.remove();

    window.URL.revokeObjectURL(
      url
    );

  } catch (error) {

    console.error(
      "PDF download failed",
      error
    );

  }

};

  if (loading) {

    return (

      <div className="p-6">

        Loading Student Strength Report...

      </div>

    );

  }

  return (

    <div className="p-6">

      {/* ================================= */}
      {/* PAGE HEADER */}
      {/* ================================= */}

      <div
        className="
          mb-6
          flex
          items-center
          justify-between
        "
      >

        <div>

          <h1
            className="
              text-2xl
              font-bold
            "
          >
            Student Strength Report
          </h1>

          <p
            className="
              mt-1
              text-gray-500
            "
          >
            Category-wise and gender-wise
            student strength
          </p>

        </div>

        <div
          className="
            flex
            gap-2
          "
        >

          <button
            onClick={handlePrint}
            className="
              rounded-lg
              bg-slate-600
              px-4
              py-2
              text-white
              hover:bg-slate-700
            "
          >
            Print
          </button>

          <button
            onClick={handleExcelDownload}
            className="
              rounded-lg
              bg-green-600
              px-4
              py-2
              text-white
              hover:bg-green-700
            "
          >
            Excel
          </button>

          <button
            onClick={handlePdfDownload}
            className="
              rounded-lg
              bg-red-600
              px-4
              py-2
              text-white
              hover:bg-red-700
            "
          >
            PDF
          </button>

        </div>

      </div>

      {/* ================================= */}
      {/* TABLE */}
      {/* ================================= */}

      <div
        className="
          overflow-x-auto
          rounded-xl
          bg-white
          shadow
        "
      >

        <table
          className="
            min-w-full
            border-collapse
          "
        >

          <thead>

            <tr
              className="
                bg-blue-700
                text-white
              "
            >

              <th
                rowSpan="2"
                className="
                  border
                  px-3
                  py-2
                "
              >
                Class
              </th>

              <th
                rowSpan="2"
                className="
                  border
                  px-3
                  py-2
                "
              >
                Section
              </th>

              <th colSpan="3" className="border px-3 py-2">
                SC
              </th>

              <th colSpan="3" className="border px-3 py-2">
                BC-A
              </th>

              <th colSpan="3" className="border px-3 py-2">
                BC-B
              </th>

              <th colSpan="3" className="border px-3 py-2">
                GEN
              </th>

              <th colSpan="3" className="border px-3 py-2">
                OVERALL
              </th>

            </tr>

            <tr
              className="
                bg-blue-500
                text-white
              "
            >

              <th>M</th>
              <th>F</th>
              <th>T</th>

              <th>M</th>
              <th>F</th>
              <th>T</th>

              <th>M</th>
              <th>F</th>
              <th>T</th>

              <th>M</th>
              <th>F</th>
              <th>T</th>

              <th>M</th>
              <th>F</th>
              <th>T</th>

            </tr>

          </thead>

          <tbody>

            {rows.map(
              (row, index) => (


                <tr
                key={index}
                className={

                    row.row_type ===
                    "grand_total"

                    ? `
                        bg-yellow-200
                        font-bold
                    `

                    : row.row_type ===
                        "class_total"

                    ? `
                        bg-blue-100
                        font-semibold
                    `

                    : `
                        even:bg-gray-50
                    `

                }
                >

                  <td
                    className="
                        border
                        px-3
                        py-2
                    "
                    >

                    {

                        row.row_type ===
                        "class_total"

                        ? `TOTAL ${row.class_name}`

                        : row.row_type ===
                            "grand_total"

                        ? "GRAND TOTAL"

                        : row.class_name

                    }

                    </td>

                    <td
                    className="
                        border
                        px-3
                        py-2
                    "
                    >

                    {

                        row.row_type ===
                        "section"

                        ? row.section_name

                        : ""

                    }

                    </td>


                  <td className="border text-center">
                    {row.sc_male}
                  </td>

                  <td className="border text-center">
                    {row.sc_female}
                  </td>

                  <td className="border text-center font-semibold">
                    {row.sc_total}
                  </td>

                  <td className="border text-center">
                    {row.bca_male}
                  </td>

                  <td className="border text-center">
                    {row.bca_female}
                  </td>

                  <td className="border text-center font-semibold">
                    {row.bca_total}
                  </td>

                  <td className="border text-center">
                    {row.bcb_male}
                  </td>

                  <td className="border text-center">
                    {row.bcb_female}
                  </td>

                  <td className="border text-center font-semibold">
                    {row.bcb_total}
                  </td>

                  <td className="border text-center">
                    {row.gen_male}
                  </td>

                  <td className="border text-center">
                    {row.gen_female}
                  </td>

                  <td className="border text-center font-semibold">
                    {row.gen_total}
                  </td>

                  <td className="border text-center">
                    {row.overall_male}
                  </td>

                  <td className="border text-center">
                    {row.overall_female}
                  </td>

                  <td
                    className="
                      border
                      text-center
                      font-bold
                    "
                  >
                    {row.overall_total}
                  </td>

                </tr>

              )
            )}

          </tbody>

        </table>

      </div>

    </div>

  );

};

export default StudentStrengthReport;