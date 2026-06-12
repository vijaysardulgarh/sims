import {
    useEffect,
    useState,
} from 'react';

import toast
    from 'react-hot-toast';

import timetableDesignerService
    from '../services/timetableDesignerService';

const TimetableConflictPage = () => {

    const [conflicts, setConflicts] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const loadConflicts =
        async () => {

            try {

                setLoading(
                    true
                );

                const response =

                    await timetableDesignerService
                        .getConflicts();

                setConflicts(

                    response.data || []

                );

            }

            catch (error) {

                console.error(
                    error
                );

                toast.error(
                    'Failed to load conflicts.'
                );

            }

            finally {

                setLoading(
                    false
                );

            }

        };

    useEffect(
        () => {

            loadConflicts();

        },
        []
    );

    return (

        <div
            className="
                max-w-7xl
                mx-auto
                space-y-6
            "
        >

            <div>

                <h1
                    className="
                        text-3xl
                        font-bold
                        text-gray-900
                    "
                >
                    Timetable Conflicts
                </h1>

                <p
                    className="
                        text-gray-500
                        mt-1
                    "
                >
                    Review and resolve timetable conflicts
                </p>

            </div>

            <div
                className="
                    bg-white
                    rounded-2xl
                    shadow
                    overflow-hidden
                "
            >

                {

                    loading

                        ? (

                            <div
                                className="
                                    p-10
                                    text-center
                                "
                            >

                                Loading...

                            </div>

                        )

                        : conflicts.length === 0

                            ? (

                                <div
                                    className="
                                        p-10
                                        text-center
                                        text-green-600
                                        font-semibold
                                    "
                                >

                                    No conflicts found

                                </div>

                            )

                            : (

                                <table
                                    className="
                                        w-full
                                    "
                                >

                                    <thead
                                        className="
                                            bg-gray-100
                                        "
                                    >

                                        <tr>

                                            <th
                                                className="
                                                    p-4
                                                    text-left
                                                "
                                            >
                                                Type
                                            </th>

                                            <th
                                                className="
                                                    p-4
                                                    text-left
                                                "
                                            >
                                                Severity
                                            </th>

                                            <th
                                                className="
                                                    p-4
                                                    text-left
                                                "
                                            >
                                                Day
                                            </th>

                                            <th
                                                className="
                                                    p-4
                                                    text-left
                                                "
                                            >
                                                Period
                                            </th>

                                            <th
                                                className="
                                                    p-4
                                                    text-left
                                                "
                                            >
                                                Message
                                            </th>

                                            <th
                                                className="
                                                    p-4
                                                    text-left
                                                "
                                            >
                                                Status
                                            </th>

                                        </tr>

                                    </thead>

                                    <tbody>

                                        {

                                            conflicts.map(
                                                (
                                                    conflict
                                                ) => (

                                                    <tr
                                                        key={
                                                            conflict.id
                                                        }
                                                        className="
                                                            border-t
                                                        "
                                                    >

                                                        <td
                                                            className="
                                                                p-4
                                                            "
                                                        >
                                                            {
                                                                conflict.type
                                                            }
                                                        </td>

                                                        <td
                                                            className="
                                                                p-4
                                                            "
                                                        >

                                                            <span
                                                                className={

                                                                    conflict.severity ===
                                                                    'CRITICAL'

                                                                        ? 'text-red-600 font-bold'

                                                                        : conflict.severity ===
                                                                          'HIGH'

                                                                            ? 'text-orange-600 font-semibold'

                                                                            : 'text-yellow-600'

                                                                }
                                                            >

                                                                {
                                                                    conflict.severity
                                                                }

                                                            </span>

                                                        </td>

                                                        <td
                                                            className="
                                                                p-4
                                                            "
                                                        >
                                                            {
                                                                conflict.day
                                                            }
                                                        </td>

                                                        <td
                                                            className="
                                                                p-4
                                                            "
                                                        >
                                                            {
                                                                conflict.period
                                                            }
                                                        </td>

                                                        <td
                                                            className="
                                                                p-4
                                                            "
                                                        >
                                                            {
                                                                conflict.message
                                                            }
                                                        </td>

                                                        <td
                                                            className="
                                                                p-4
                                                            "
                                                        >
                                                            {
                                                                conflict.status
                                                            }
                                                        </td>

                                                    </tr>

                                                )
                                            )

                                        }

                                    </tbody>

                                </table>

                            )

                }

            </div>

        </div>

    );

};

export default TimetableConflictPage;