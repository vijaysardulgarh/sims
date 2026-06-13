const TimetableStatistics = ({
    totalEntries = 0,
    totalConflicts = 0,
    totalTeachers = 0,
}) => {

    return (

        <div
            className="
                grid
                grid-cols-3
                gap-4
            "
        >

            <div
                className="
                    bg-white
                    border
                    rounded-lg
                    p-4
                "
            >

                <div
                    className="
                        text-sm
                        text-gray-500
                    "
                >
                    Entries
                </div>

                <div
                    className="
                        text-2xl
                        font-bold
                    "
                >
                    {totalEntries}
                </div>

            </div>

            <div
                className="
                    bg-white
                    border
                    rounded-lg
                    p-4
                "
            >

                <div
                    className="
                        text-sm
                        text-gray-500
                    "
                >
                    Conflicts
                </div>

                <div
                    className="
                        text-2xl
                        font-bold
                    "
                >
                    {totalConflicts}
                </div>

            </div>

            <div
                className="
                    bg-white
                    border
                    rounded-lg
                    p-4
                "
            >

                <div
                    className="
                        text-sm
                        text-gray-500
                    "
                >
                    Teachers
                </div>

                <div
                    className="
                        text-2xl
                        font-bold
                    "
                >
                    {totalTeachers}
                </div>

            </div>

        </div>

    );

};

export default TimetableStatistics;