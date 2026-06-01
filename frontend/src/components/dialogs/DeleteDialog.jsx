import React from "react";
import Button from "../ui/Button";

const DeleteDialog = ({
    open,
    onDelete,
    onCancel,
    loading = false,
}) => {
    if (!open) return null;

    return (
        <>
            <div
                className="
                    fixed
                    inset-0
                    bg-black/40
                    z-40
                "
                onClick={onCancel}
            />

            <div
                className="
                    fixed
                    inset-0
                    flex
                    items-center
                    justify-center
                    z-50
                "
            >
                <div
                    className="
                        bg-white
                        rounded-lg
                        shadow-xl
                        w-full
                        max-w-md
                        p-6
                    "
                >
                    <h2
                        className="
                            text-lg
                            font-semibold
                            text-red-600
                            mb-3
                        "
                    >
                        Delete Record
                    </h2>

                    <p className="text-gray-600 mb-6">
                        Are you sure you want to
                        delete this record?
                    </p>

                    <div
                        className="
                            flex
                            justify-end
                            gap-3
                        "
                    >
                        <Button
                            variant="secondary"
                            onClick={onCancel}
                        >
                            Cancel
                        </Button>

                        <Button
                            variant="danger"
                            onClick={onDelete}
                            disabled={loading}
                        >
                            Delete
                        </Button>
                    </div>
                </div>
            </div>
        </>
    );
};

export default DeleteDialog;