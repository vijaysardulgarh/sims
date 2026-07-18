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

                {/* =========================
                    TABLE HEADER
                ========================= */}

                <thead className="bg-gray-100">

                    <tr>

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
                            Sr. No.
                        </th>

                        {
                            columns.map((column) => (

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

                            ))
                        }

                    </tr>

                </thead>

                {/* =========================
                    TABLE BODY
                ========================= */}

                <tbody>

                    {
                        data.length > 0 ? (

                            data.map((row, index) => (

                                <tr
                                    key={row.id || index}
                                    className="
                                        border-b
                                        hover:bg-gray-50
                                    "
                                >

                                    {/* SR NO */}

                                    <td
                                        className="
                                            px-6
                                            py-4
                                            text-sm
                                            font-medium
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

                                    {/* DYNAMIC COLUMNS */}

                                    {
                                        columns.map((column) => (

                                            <td
                                                key={`${index}-${column.key}`}
                                                className="
                                                    px-6
                                                    py-4
                                                    text-sm
                                                    text-gray-600
                                                "
                                            >

                                                {
                                                    column.render
                                                        ? column.render(row)
                                                        : row[column.key]
                                                }

                                            </td>

                                        ))
                                    }

                                </tr>

                            ))

                        ) : (

                            <tr>

                                <td
                                    colSpan={
                                        columns.length + 1
                                    }
                                    className="
                                        px-6
                                        py-10
                                        text-center
                                        text-gray-500
                                    "
                                >
                                    No records found
                                </td>

                            </tr>

                        )
                    }

                </tbody>

            </table>

        </div>

    );

};

export default DataTable;