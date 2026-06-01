const SkeletonLoader = ({
    rows = 5,
}) => {
    return (
        <div className="space-y-3">
            {Array.from({
                length: rows,
            }).map((_, index) => (
                <div
                    key={index}
                    className="
                        h-10
                        rounded-md
                        bg-gray-200
                        animate-pulse
                    "
                />
            ))}
        </div>
    );
};

export default SkeletonLoader;