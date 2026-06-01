const DateInput = ({
    label,
    name,
    value,
    onChange,
    required = false,
    error = "",
}) => {
    return (
        <div className="space-y-1">
            {label && (
                <label className="block text-sm font-medium">
                    {label}
                </label>
            )}

            <input
                type="date"
                name={name}
                value={value}
                onChange={onChange}
                required={required}
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
            />

            {error && (
                <p className="text-red-500 text-sm">
                    {error}
                </p>
            )}
        </div>
    );
};

export default DateInput;