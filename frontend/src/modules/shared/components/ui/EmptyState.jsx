const EmptyState = ({
    title = "No Records Found",
}) => {
    return (
        <div
            className="
                flex
                items-center
                justify-center
                py-10
                text-gray-500
            "
        >
            {title}
        </div>
    );
};

export default EmptyState;