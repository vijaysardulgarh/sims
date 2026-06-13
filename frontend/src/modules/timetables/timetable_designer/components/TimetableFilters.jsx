const TimetableFilters = ({
    schools = [],
    classes = [],
    sections = [],
}) => {

    return (

        <div
            className="
                bg-white
                border
                rounded-lg
                p-4
                grid
                grid-cols-3
                gap-4
            "
        >

            <select
                className="
                    border
                    rounded-lg
                    p-2
                "
            >

                <option>
                    Select School
                </option>

            </select>

            <select
                className="
                    border
                    rounded-lg
                    p-2
                "
            >

                <option>
                    Select Class
                </option>

            </select>

            <select
                className="
                    border
                    rounded-lg
                    p-2
                "
            >

                <option>
                    Select Section
                </option>

            </select>

        </div>

    );

};

export default TimetableFilters;