// src/components/ui/Card.jsx

import React from "react";

const Card = ({
    title,
    children,
    className = "",
}) => {
    return (
        <div
            className={`
                bg-white
                border
                rounded-lg
                shadow-sm
                p-5
                ${className}
            `}
        >
            {title && (
                <h3
                    className="
                        text-lg
                        font-semibold
                        mb-4
                    "
                >
                    {title}
                </h3>
            )}

            {children}
        </div>
    );
};

export default Card;