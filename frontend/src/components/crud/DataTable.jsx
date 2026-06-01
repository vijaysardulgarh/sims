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
            "
        >

            <table className="w-full">

                <thead
                    className="
                        bg-gray-100
                        sticky
                        top-0
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
                                    "
                                >
                                    {column.label}
                                </th>
                            )
                        )}

                        <th
                            className="
                                px-4
                                py-3
                                text-left
                            "
                        >
                            Actions
                        </th>

                    </tr>
                </thead>

                <tbody>

                    {data.map((row) => (

                        <tr
                            key={row.id}
                            className="
                                border-t
                            "
                        >

                            {columns.map(
                                (column) => (
                                    <td
                                        key={
                                            column.key
                                        }
                                        className="
                                            px-4
                                            py-3
                                        "
                                    >
                                        {
                                            row[
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