import TimetableCell
    from './TimetableCell';

const TimetableGrid = ({
    entries = [],
}) => {

    const days = [

        'MONDAY',
        'TUESDAY',
        'WEDNESDAY',
        'THURSDAY',
        'FRIDAY',
        'SATURDAY',

    ];

    const periods = [

        1, 2, 3, 4, 5, 6, 7, 8,

    ];

    return (

        <div
            className="
                overflow-auto
            "
        >

            <table
                className="
                    min-w-full
                    border
                "
            >

                <thead>

                    <tr>

                        <th>
                            Period
                        </th>

                        {

                            days.map(
                                day => (

                                    <th
                                        key={day}
                                    >
                                        {day}
                                    </th>

                                )
                            )

                        }

                    </tr>

                </thead>

                <tbody>

                    {

                        periods.map(
                            period => (

                                <tr
                                    key={period}
                                >

                                    <td>
                                        {period}
                                    </td>

                                    {

                                        days.map(
                                            day => {

                                                const entry =

                                                    entries.find(

                                                        item =>

                                                            item.day === day &&

                                                            item.period === period

                                                    );

                                                return (

                                                    <td
                                                        key={`${day}-${period}`}
                                                    >

                                                        <TimetableCell
                                                            entry={entry}
                                                        />

                                                    </td>

                                                );

                                            }
                                        )

                                    }

                                </tr>

                            )
                        )

                    }

                </tbody>

            </table>

        </div>

    );

};

export default TimetableGrid;