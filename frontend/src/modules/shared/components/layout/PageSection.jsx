const PageSection = ({
    title,
    children,
}) => {
    return (
        <div
            className="
                bg-white
                border
                rounded-xl
                shadow-sm
            "
        >
            {title && (
                <div
                    className="
                        px-5
                        py-4
                        border-b
                        font-semibold
                    "
                >
                    {title}
                </div>
            )}

            <div className="p-5">
                {children}
            </div>
        </div>
    );
};

export default PageSection;