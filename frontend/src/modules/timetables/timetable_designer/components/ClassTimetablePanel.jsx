const ClassTimetablePanel = ({
    entries = [],
}) => {

    return (

        <div
            className="
                bg-white
                border
                rounded-lg
                p-4
            "
        >

            <h3
                className="
                    font-semibold
                    mb-3
                "
            >
                Class Timetable
            </h3>

            <div
                className="
                    space-y-2
                "
            >

                {

                    entries.map(
                        entry => (

                            <div
                                key={entry.id}
                                className="
                                    border-b
                                    pb-2
                                "
                            >

                                {entry.day}
                                {' '}
                                -
                                {' '}
                                {entry.period_name}

                            </div>

                        )
                    )

                }

            </div>

        </div>

    );

};

export default ClassTimetablePanel;