const TimetableToolbar = ({
    onGenerate,
}) => {

    return (

        <div
            className="
                flex
                gap-3
                mb-4
            "
        >

            <button

                onClick={
                    onGenerate
                }

                className="
                    px-4
                    py-2
                    bg-blue-600
                    text-white
                    rounded-lg
                "
            >

                Generate Timetable

            </button>

        </div>

    );

};

export default TimetableToolbar;