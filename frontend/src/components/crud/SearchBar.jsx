import React from "react";

const SearchBar = ({
    value,
    onChange,
    placeholder = "Search..."
}) => {
    return (
        <input
            type="text"
            value={value}
            onChange={(e) => onChange(e.target.value)}
            placeholder={placeholder}
            className="
                w-full
                md:w-80
                border
                rounded-md
                px-3
                py-2
                focus:outline-none
                focus:ring-2
                focus:ring-blue-500
            "
        />
    );
};

export default SearchBar;