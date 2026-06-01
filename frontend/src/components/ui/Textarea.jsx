// src/components/ui/Textarea.jsx

import React from "react";

const Textarea = ({
    label,
    name,
    value,
    onChange,
    placeholder = "",
    rows = 4,
    required = false,
    error = "",
}) => {
    return (
        <div className="space-y-1">
            {label && (
                <label className="block text-sm font-medium text-gray-700">
                    {label}
                </label>
            )}

            <textarea
                name={name}
                value={value}
                onChange={onChange}
                placeholder={placeholder}
                rows={rows}
                required={required}
                className="
                    w-full
                    px-3
                    py-2
                    border
                    rounded-md
                    focus:outline-none
                    focus:ring-2
                    focus:ring-blue-500
                "
            />

            {error && (
                <p className="text-sm text-red-500">
                    {error}
                </p>
            )}
        </div>
    );
};

export default Textarea;