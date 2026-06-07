import React from "react";

const Select = ({
    label,
    name,
    value,
    onChange,
    options = [],
    error = "",
}) => {
    return (
        <div className="space-y-1">
            {label && (
                <label className="block text-sm font-medium">
                    {label}
                </label>
            )}

            <select
                name={name}
                value={value}
                onChange={onChange}
                className="
                    w-full
                    border
                    rounded-md
                    px-3
                    py-2
                    focus:outline-none
                    focus:ring-2
                    focus:ring-blue-500
                "
            >
                <option value="">
                    Select
                </option>

                {options.map((option) => (
                    <option
                        key={option.value}
                        value={option.value}
                    >
                        {option.label}
                    </option>
                ))}
            </select>

            {error && (
                <p className="text-red-500 text-sm">
                    {error}
                </p>
            )}
        </div>
    );
};

export default Select;