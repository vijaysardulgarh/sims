const StatsCard = ({
    title,
    value,
    icon,
}) => {
    return (
        <div
            className="
                bg-white
                border
                rounded-xl
                shadow-sm
                p-5
            "
        >
            <div
                className="
                    flex
                    justify-between
                    items-center
                "
            >
                <div>
                    <p
                        className="
                            text-sm
                            text-gray-500
                        "
                    >
                        {title}
                    </p>

                    <h3
                        className="
                            text-2xl
                            font-bold
                            mt-1
                        "
                    >
                        {value}
                    </h3>
                </div>

                {icon}
            </div>
        </div>
    );
};

export default StatsCard;