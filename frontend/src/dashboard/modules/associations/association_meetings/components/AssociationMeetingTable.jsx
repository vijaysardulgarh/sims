// ============================================
// IMPORTS
// ============================================

import { Link } from 'react-router-dom';

// ============================================
// COMPONENT
// ============================================

const AssociationMeetingTable = ({
    meetings,
    onDelete,
}) => {

    return (

        <div className="overflow-x-auto bg-white rounded-2xl shadow">

            <table className="min-w-full divide-y divide-gray-200">

                {/* ================================= */}
                {/* HEADER */}
                {/* ================================= */}

                <thead className="bg-gray-50">

                    <tr>

                        <th className="px-4 py-3 text-left">
                            ID
                        </th>

                        <th className="px-4 py-3 text-left">
                            Association
                        </th>

                        <th className="px-4 py-3 text-left">
                            Meeting Date
                        </th>

                        <th className="px-4 py-3 text-left">
                            Location
                        </th>

                        <th className="px-4 py-3 text-left">
                            Agenda
                        </th>

                        <th className="px-4 py-3 text-center">
                            Actions
                        </th>

                    </tr>

                </thead>

                {/* ================================= */}
                {/* BODY */}
                {/* ================================= */}

                <tbody className="divide-y divide-gray-200">

                    {
                        meetings?.length > 0 ? (

                            meetings.map((meeting) => (

                                <tr
                                    key={meeting.id}
                                    className="hover:bg-gray-50"
                                >

                                    <td className="px-4 py-3">
                                        {meeting.id}
                                    </td>

                                    <td className="px-4 py-3">
                                        {meeting.association}
                                    </td>

                                    <td className="px-4 py-3">
                                        {
                                            meeting.meeting_date
                                                ? new Date(
                                                    meeting.meeting_date
                                                ).toLocaleString()
                                                : '-'
                                        }
                                    </td>

                                    <td className="px-4 py-3">
                                        {meeting.location}
                                    </td>

                                    <td className="px-4 py-3">

                                        {
                                            meeting.agenda
                                                ?.length > 50

                                                ? `${meeting.agenda.substring(
                                                    0,
                                                    50
                                                )}...`

                                                : meeting.agenda
                                        }

                                    </td>

                                    <td className="px-4 py-3">

                                        <div className="flex justify-center gap-2">

                                            <Link
                                                to={`/dashboard/associations/association-meetings/${meeting.id}`}
                                                className="px-3 py-1 text-sm bg-blue-500 text-white rounded"
                                            >
                                                View
                                            </Link>

                                            <Link
                                                to={`/dashboard/associations/association-meetings/edit/${meeting.id}`}
                                                className="px-3 py-1 text-sm bg-yellow-500 text-white rounded"
                                            >
                                                Edit
                                            </Link>

                                            <button
                                                onClick={() =>
                                                    onDelete(
                                                        meeting.id
                                                    )
                                                }
                                                className="px-3 py-1 text-sm bg-red-500 text-white rounded"
                                            >
                                                Delete
                                            </button>

                                        </div>

                                    </td>

                                </tr>

                            ))

                        ) : (

                            <tr>

                                <td
                                    colSpan="6"
                                    className="px-4 py-6 text-center text-gray-500"
                                >
                                    No meetings found.
                                </td>

                            </tr>

                        )
                    }

                </tbody>

            </table>

        </div>
    );
};

export default AssociationMeetingTable;