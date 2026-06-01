// src/components/ui/Checkbox.jsx

import React from "react";

const Checkbox = ({
    label,
    name,
    checked = false,
    onChange,
    disabled = false,
}) => {
    return (
        <label className="flex items-center gap-2 cursor-pointer">
            <input
                type="checkbox"
                name={name}
                checked={checked}
                onChange={onChange}
                disabled={disabled}
                className="
                    h-4
                    w-4
                    rounded
                    border-gray-300
                "
            />

            <span className="text-sm text-gray-700">
                {label}
            </span>
        </label>
    );
};

export default Checkbox;