// src/components/ui/Badge.jsx

import React from "react";

const variants = {
    success:
        "bg-green-100 text-green-700",

    danger:
        "bg-red-100 text-red-700",

    warning:
        "bg-yellow-100 text-yellow-700",

    primary:
        "bg-blue-100 text-blue-700",

    secondary:
        "bg-gray-100 text-gray-700",
};

const Badge = ({
    children,
    variant = "primary",
}) => {
    return (
        <span
            className={`
                inline-flex
                items-center
                px-2.5
                py-1
                rounded-full
                text-xs
                font-medium
                ${variants[variant]}
            `}
        >
            {children}
        </span>
    );
};

export default Badge;