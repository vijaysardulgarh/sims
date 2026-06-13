import TimetableCell
    from './TimetableCell';

import DroppableCell
    from './DroppableCell';

const TimetableGrid = ({
    entries = [],
}) => {

    const days = [

        {
            code: 'MON',
            label: 'Monday',
        },

        {
            code: 'TUE',
            label: 'Tuesday',
        },

        {
            code: 'WED',
            label: 'Wednesday',
        },

        {
            code: 'THU',
            label: 'Thursday',
        },

        {
            code: 'FRI',
            label: 'Friday',
        },

        {
            code: 'SAT',
            label: 'Saturday',
        },

    ];

    const periods = [

        ...new Set(

            entries.map(
                entry => entry.period_number
            )

        ),

    ].sort(
        (
            a,
            b
        ) => a - b
    );

    return (

        <div
            className="
                overflow-auto
                rounded-lg
                border
                bg-white
            "
        >

            <table
                className="
                    min-w-full
                    border-collapse
                "
            >

                <thead>

                    <tr
                        className="
                            bg-gray-100
                        "
                    >

                        <th
                            className="
                                border
                                p-3
                                text-center
                                font-semibold
                            "
                        >
                            Period
                        </th>

                        {

                            days.map(
                                day => (

                                    <th
                                        key={day.code}
                                        className="
                                            border
                                            p-3
                                            text-center
                                            font-semibold
                                        "
                                    >

                                        {day.label}

                                    </th>

                                )
                            )

                        }

                    </tr>

                </thead>

                <tbody>

                    {

                        periods.length > 0

                            ?

                            periods.map(
                                period => (

                                    <tr
                                        key={period}
                                    >

                                        <td
                                            className="
                                                border
                                                p-3
                                                text-center
                                                font-semibold
                                                bg-gray-50
                                            "
                                        >

                                            {period}

                                        </td>

                                        {

                                            days.map(
                                                day => {

                                                    const entry =

                                                        entries.find(

                                                            item =>

                                                                item.day === day.code &&

                                                                item.period_number === period

                                                        );

                                                    const cellId =

                                                        `cell-${day.code}-${period}`;

                                                    return (

                                                        <td
                                                            key={cellId}
                                                            className="
                                                                border
                                                                p-2
                                                                min-w-[180px]
                                                                h-[90px]
                                                                align-top
                                                            "
                                                        >

                                                            <DroppableCell

                                                                id={
                                                                    cellId
                                                                }

                                                                entryId={
                                                                    entry?.id
                                                                }

                                                            >

                                                                <TimetableCell
                                                                    entry={entry}
                                                                />

                                                            </DroppableCell>

                                                        </td>

                                                    );

                                                }
                                            )

                                        }

                                    </tr>

                                )
                            )

                            :

                            (

                                <tr>

                                    <td
                                        colSpan={7}
                                        className="
                                            p-6
                                            text-center
                                            text-gray-500
                                        "
                                    >

                                        No timetable entries found

                                    </td>

                                </tr>

                            )

                    }

                </tbody>

            </table>

        </div>

    );

};

export default TimetableGrid;