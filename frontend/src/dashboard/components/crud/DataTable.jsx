import React from "react";

const DataTable = ({
  columns = [],
  data = [],
  currentPage = 1,
  itemsPerPage = 40,
}) => {

  return (

    <div className="overflow-x-auto bg-white rounded-2xl shadow">

      <table className="min-w-full">

        {/* TABLE HEADER */}

        <thead className="bg-gray-100">

          <tr>

            {

              columns.map((column, index) => {

                // =========================
                // AFTER SELECT ADD SR NO
                // =========================

                if (index === 1) {

                  return (

                    <React.Fragment
                      key={`header-${column.key}`}
                    >

                      <th
                        className="
                          px-6
                          py-4
                          text-left
                          text-sm
                          font-semibold
                          text-gray-700
                        "
                      >
                        Sr. No
                      </th>

                      <th
                        className="
                          px-6
                          py-4
                          text-left
                          text-sm
                          font-semibold
                          text-gray-700
                        "
                      >

                        {column.label}

                      </th>

                    </React.Fragment>
                  );
                }

                return (

                  <th
                    key={column.key}
                    className="
                      px-6
                      py-4
                      text-left
                      text-sm
                      font-semibold
                      text-gray-700
                    "
                  >

                    {column.label}

                  </th>
                );
              })
            }

          </tr>

        </thead>

        {/* TABLE BODY */}

        <tbody>

          {

            data.map((row, index) => (

              <tr
                key={row.id || index}
                className="border-b"
              >

                {

                  columns.map((column, columnIndex) => {

                    // =====================
                    // INSERT SR NO COLUMN
                    // =====================

                    if (columnIndex === 1) {

                      return (

                        <React.Fragment
                          key={`body-${index}-${column.key}`}
                        >

                          <td
                            className="
                              px-6
                              py-4
                              text-sm
                              font-semibold
                              text-gray-700
                            "
                          >

                            {

                              (
                                (currentPage - 1)

                                *

                                itemsPerPage
                              )

                              +

                              index

                              +

                              1
                            }

                          </td>

                          <td
                            className="
                              px-6
                              py-4
                              text-sm
                              text-gray-600
                            "
                          >

                            {row[column.key]}

                          </td>

                        </React.Fragment>
                      );
                    }

                    return (

                      <td
                        key={`${index}-${column.key}`}
                        className="
                          px-6
                          py-4
                          text-sm
                          text-gray-600
                        "
                      >

                        {row[column.key]}

                      </td>
                    );
                  })
                }

              </tr>
            ))
          }

        </tbody>

      </table>

    </div>
  );
};

export default DataTable;