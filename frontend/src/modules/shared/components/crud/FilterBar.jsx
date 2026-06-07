const FilterBar = ({
    children,
}) => {
    return (
        <div
            className="
                bg-white
                border
                rounded-lg
                p-4
                flex
                flex-wrap
                gap-4
                items-end
            "
        >
            {children}
        </div>
    );
};

export default FilterBar;