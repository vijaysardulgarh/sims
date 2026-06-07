import React, { useEffect } from "react";

const CrudDrawer = ({
    open,
    title,
    children,
    onClose,
    tabs = [],
    activeTab,
    onTabChange,
}) => {

    useEffect(() => {

        const handleEscape = (event) => {
            if (event.key === "Escape") {
                onClose();
            }
        };

        if (open) {
            document.addEventListener(
                "keydown",
                handleEscape
            );
        }

        return () => {
            document.removeEventListener(
                "keydown",
                handleEscape
            );
        };

    }, [open, onClose]);

    if (!open) return null;

    return (
        <>
            {/* Overlay */}

            <div
                className="
                    fixed
                    inset-0
                    bg-black/40
                    z-40
                "
                onClick={onClose}
            />

            {/* Drawer */}

            <div
                className="
                    fixed
                    top-0
                    right-0
                    h-screen
                    bg-white
                    shadow-xl
                    z-50
                    flex
                    flex-col
                    w-full
                    md:w-[700px]
                "
            >
                {/* Header */}

                <div
                    className="
                        px-6
                        py-4
                        border-b
                        flex
                        justify-between
                        items-center
                    "
                >
                    <h2
                        className="
                            text-lg
                            font-semibold
                        "
                    >
                        {title}
                    </h2>

                    <button
                        onClick={onClose}
                        className="
                            text-2xl
                            text-gray-500
                            hover:text-black
                        "
                    >
                        ×
                    </button>
                </div>

                {/* Tabs */}

                {tabs.length > 0 && (
                    <div
                        className="
                            flex
                            border-b
                            overflow-x-auto
                        "
                    >
                        {tabs.map((tab) => (

                            <button
                                key={tab}
                                onClick={() =>
                                    onTabChange(tab)
                                }
                                className={`
                                    px-4
                                    py-3
                                    whitespace-nowrap
                                    border-b-2
                                    ${
                                        activeTab === tab
                                            ? "border-blue-600 text-blue-600"
                                            : "border-transparent text-gray-500"
                                    }
                                `}
                            >
                                {tab}
                            </button>

                        ))}
                    </div>
                )}

                {/* Content */}

                <div
                    className="
                        flex-1
                        overflow-y-auto
                        p-6
                    "
                >
                    {children}
                </div>

            </div>
        </>
    );
};

export default CrudDrawer;