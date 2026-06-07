import React, { useState } from "react";

const TableActionMenu = ({
    row,
    onView,
    onEdit,
    onDelete,
    onDuplicate,
}) => {

    const [open, setOpen] =
        useState(false);

    return (
        <div className="relative">

            <button
                onClick={() =>
                    setOpen(!open)
                }
                className="
                    px-2
                    py-1
                    border
                    rounded
                "
            >
                ⋮
            </button>

            {open && (
                <div
                    className="
                        absolute
                        right-0
                        mt-1
                        bg-white
                        border
                        rounded-md
                        shadow-lg
                        w-40
                        z-50
                    "
                >

                    <button
                        onClick={() =>
                            onView?.(row)
                        }
                        className="
                            block
                            w-full
                            text-left
                            px-4
                            py-2
                            hover:bg-gray-100
                        "
                    >
                        View
                    </button>

                    <button
                        onClick={() =>
                            onEdit?.(row)
                        }
                        className="
                            block
                            w-full
                            text-left
                            px-4
                            py-2
                            hover:bg-gray-100
                        "
                    >
                        Edit
                    </button>

                    <button
                        onClick={() =>
                            onDuplicate?.(row)
                        }
                        className="
                            block
                            w-full
                            text-left
                            px-4
                            py-2
                            hover:bg-gray-100
                        "
                    >
                        Duplicate
                    </button>

                    <button
                        onClick={() =>
                            onDelete?.(row)
                        }
                        className="
                            block
                            w-full
                            text-left
                            px-4
                            py-2
                            text-red-600
                            hover:bg-gray-100
                        "
                    >
                        Delete
                    </button>

                </div>
            )}

        </div>
    );
};

export default TableActionMenu;