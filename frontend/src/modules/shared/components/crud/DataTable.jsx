import React from "react";

import TableActionMenu
from "./TableActionMenu";

const DataTable = ({
    columns,
    data,
    onView,
    onEdit,
    onDelete,
}) => {

    return (

        <div
            className="
                overflow-x-auto
                border
                rounded-lg
                bg-white
            "
        >

            <table className="w-full">

                <thead
                    className="
                        bg-gray-50
                    "
                >
                    <tr>

                        {columns.map(
                            (column) => (
                                <th
                                    key={column.key}
                                    className="
                                        px-4
                                        py-3
                                        text-left
                                        font-semibold
                                        text-gray-700
                                    "
                                >
                                    {column.label}
                                </th>
                            )
                        )}

                        <th
                            className="
                                w-16
                                text-center
                            "
                        >
                        </th>

                    </tr>
                </thead>

                <tbody>

                    {data.length === 0 && (

                        <tr>

                            <td
                                colSpan={
                                    columns.length + 1
                                }
                                className="
                                    text-center
                                    py-10
                                    text-gray-500
                                "
                            >
                                No records found
                            </td>

                        </tr>

                    )}

                    {data.map((row) => (

                        <tr
                            key={row.id}
                            className="
                                border-t
                                hover:bg-gray-50
                            "
                        >

                            {columns.map(
                                (column) => (

                                    <td
                                        key={column.key}
                                        className="
                                            px-4
                                            py-3
                                        "
                                    >

                                        {
                                            column.render
                                                ? column.render(
                                                      row
                                                  )
                                                : row[
                                                      column.key
                                                  ]
                                        }

                                    </td>

                                )
                            )}

                            <td
                                className="
                                    px-4
                                    py-3
                                    text-center
                                "
                            >

                                <TableActionMenu
                                    row={row}
                                    onView={onView}
                                    onEdit={onEdit}
                                    onDelete={onDelete}
                                />

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );
};

export default DataTable;