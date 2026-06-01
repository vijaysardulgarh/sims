// src/components/ui/Switch.jsx

import React from "react";

const Switch = ({
    checked = false,
    onChange,
    label = "",
}) => {
    return (
        <div className="flex items-center gap-3">
            {label && (
                <span className="text-sm text-gray-700">
                    {label}
                </span>
            )}

            <button
                type="button"
                onClick={onChange}
                className={`
                    relative
                    inline-flex
                    h-6
                    w-11
                    items-center
                    rounded-full
                    transition
                    ${
                        checked
                            ? "bg-blue-600"
                            : "bg-gray-300"
                    }
                `}
            >
                <span
                    className={`
                        inline-block
                        h-4
                        w-4
                        transform
                        rounded-full
                        bg-white
                        transition
                        ${
                            checked
                                ? "translate-x-6"
                                : "translate-x-1"
                        }
                    `}
                />
            </button>
        </div>
    );
};

export default Switch;