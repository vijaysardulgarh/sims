// ============================================
// IMPORTS
// ============================================

import {
    useEffect,
    useState,
} from 'react';

import {
    Link,
} from 'react-router-dom';

import associationMeetingService from '../services/associationMeetingService';

// ============================================
// COMPONENT
// ============================================

const AssociationMeetingListPage = () => {

    const [meetings, setMeetings] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    useEffect(() => {

        fetchMeetings();

    }, []);

    // ========================================
    // FETCH MEETINGS
    // ========================================

    const fetchMeetings = async () => {

        try {

            const response =
                await associationMeetingService.getAll();

            console.log(
                'Association Meetings Response:',
                response
            );

            setMeetings(

                response?.data?.data ||

                response?.data ||

                []
            );

        } catch (error) {

            console.error(
                'Error fetching meetings:',
                error
            );

            setMeetings([]);
        }

        finally {

            setLoading(false);
        }
    };

    // ========================================
    // DELETE
    // ========================================

    const handleDelete = async (id) => {

        const confirmed =
            window.confirm(
                'Delete this meeting?'
            );

        if (!confirmed) {

            return;
        }

        try {

            await associationMeetingService.delete(
                id
            );

            fetchMeetings();

        } catch (error) {

            console.error(error);
        }
    };

    // ========================================
    // LOADING
    // ========================================

    if (loading) {

        return (

            <div className="p-6">
                Loading...
            </div>
        );
    }

    // ========================================
    // PAGE
    // ========================================

    return (

        <div className="p-6">

            <div className="flex justify-between items-center mb-6">

                <h1 className="text-2xl font-bold">

                    Association Meetings

                </h1>

                <Link
                    to="/dashboard/associations/association-meetings/create"
                    className="px-4 py-2 bg-blue-600 text-white rounded"
                >
                    Add Meeting
                </Link>

            </div>

            <div className="overflow-x-auto bg-white rounded-xl shadow">

                <table className="w-full">

                    <thead>

                        <tr className="border-b">

                            <th className="p-3 text-left">
                                ID
                            </th>

                            <th className="p-3 text-left">
                                Association
                            </th>

                            <th className="p-3 text-left">
                                Meeting Date
                            </th>

                            <th className="p-3 text-left">
                                Location
                            </th>

                            <th className="p-3 text-center">
                                Actions
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {
                            meetings.length > 0 ? (

                                meetings.map((meeting) => (

                                    <tr
                                        key={meeting.id}
                                        className="border-b"
                                    >

                                        <td className="p-3">
                                            {meeting.id}
                                        </td>

                                        <td className="p-3">
                                            {meeting.association}
                                        </td>

                                        <td className="p-3">
                                            {meeting.meeting_date}
                                        </td>

                                        <td className="p-3">
                                            {meeting.location}
                                        </td>

                                        <td className="p-3">

                                            <div className="flex justify-center gap-2">

                                                <Link
                                                    to={`/dashboard/associations/association-meetings/${meeting.id}`}
                                                    className="px-3 py-1 bg-blue-500 text-white rounded"
                                                >
                                                    View
                                                </Link>

                                                <Link
                                                    to={`/dashboard/associations/association-meetings/edit/${meeting.id}`}
                                                    className="px-3 py-1 bg-yellow-500 text-white rounded"
                                                >
                                                    Edit
                                                </Link>

                                                <button
                                                    onClick={() =>
                                                        handleDelete(
                                                            meeting.id
                                                        )
                                                    }
                                                    className="px-3 py-1 bg-red-500 text-white rounded"
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
                                        colSpan="5"
                                        className="p-6 text-center text-gray-500"
                                    >
                                        No meetings found
                                    </td>

                                </tr>

                            )
                        }

                    </tbody>

                </table>

            </div>

        </div>
    );
};

export default AssociationMeetingListPage;