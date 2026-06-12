const TimetableCell = ({
    entry,
}) => {

    if (!entry) {

        return (

            <div
                className="
                    h-24
                    border
                    rounded-lg
                    bg-white
                "
            />

        );

    }

    return (

        <div
            className="
                h-24
                border
                rounded-lg
                bg-blue-50
                p-2
                cursor-move
            "
        >

            <div
                className="
                    font-semibold
                "
            >
                {entry.subject_name}
            </div>

            <div
                className="
                    text-sm
                    text-gray-600
                "
            >
                {entry.teacher_name}
            </div>

            <div
                className="
                    text-xs
                    text-gray-500
                "
            >
                {entry.room_name}
            </div>

        </div>

    );

};

export default TimetableCell;