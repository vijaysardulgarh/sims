const DateTimeInput = ({
    label,
    name,
    value,
    onChange,
}) => {
    return (
        <div className="space-y-1">
            {label && (
                <label className="block text-sm font-medium">
                    {label}
                </label>
            )}

            <input
                type="datetime-local"
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
            />
        </div>
    );
};

export default DateTimeInput;