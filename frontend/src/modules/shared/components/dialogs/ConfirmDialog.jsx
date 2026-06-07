import React from "react";
import Button from "../ui/Button";

const ConfirmDialog = ({
    open,
    title = "Confirm Action",
    message = "Are you sure?",
    onConfirm,
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
                            mb-3
                        "
                    >
                        {title}
                    </h2>

                    <p className="text-gray-600 mb-6">
                        {message}
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
                            variant="primary"
                            onClick={onConfirm}
                            disabled={loading}
                        >
                            Confirm
                        </Button>
                    </div>
                </div>
            </div>
        </>
    );
};

export default ConfirmDialog;