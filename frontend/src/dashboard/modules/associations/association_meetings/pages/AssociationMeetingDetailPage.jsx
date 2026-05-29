// ============================================
// IMPORTS
// ============================================

import {
    useEffect,
    useState,
} from 'react';

import {
    Link,
    useParams,
} from 'react-router-dom';

import associationMeetingService from '../services/associationMeetingService';

// ============================================
// COMPONENT
// ============================================

const AssociationMeetingDetailPage = () => {

    const { id } = useParams();

    const [meeting, setMeeting] =
        useState(null);

    const [loading, setLoading] =
        useState(true);

    // ========================================
    // LOAD DATA
    // ========================================

    useEffect(() => {

        fetchMeeting();

    }, [id]);

    // ========================================
    // FETCH MEETING
    // ========================================

    const fetchMeeting = async () => {

        try {

            const response =
                await associationMeetingService.getById(
                    id
                );

            console.log(
                'Meeting Detail:',
                response
            );

            setMeeting(

                response?.data?.data ||

                response?.data ||

                null
            );

        } catch (error) {

            console.error(error);
        }

        finally {

            setLoading(false);
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
    // NOT FOUND
    // ========================================

    if (!meeting) {

        return (

            <div className="p-6">

                Meeting not found

            </div>
        );
    }

    // ========================================
    // PAGE
    // ========================================

    return (

        <div className="p-6 max-w-4xl mx-auto">

            <div className="flex justify-between items-center mb-6">

                <h1 className="text-3xl font-bold">

                    Association Meeting Details

                </h1>

                <Link
                    to="/dashboard/associations/association-meetings"
                    className="px-4 py-2 bg-gray-600 text-white rounded"
                >
                    Back
                </Link>

            </div>

            <div className="bg-white shadow rounded-xl p-6">

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                    <div>

                        <label className="font-semibold">

                            ID

                        </label>

                        <p className="mt-1">

                            {meeting.id}

                        </p>

                    </div>

                    <div>

                        <label className="font-semibold">

                            Association

                        </label>

                        <p className="mt-1">

                            {
                                meeting.association_name ||

                                meeting.association ||

                                '-'
                            }

                        </p>

                    </div>

                    <div>

                        <label className="font-semibold">

                            Meeting Date

                        </label>

                        <p className="mt-1">

                            {
                                meeting.meeting_date ||

                                '-'
                            }

                        </p>

                    </div>

                    <div>

                        <label className="font-semibold">

                            Location

                        </label>

                        <p className="mt-1">

                            {
                                meeting.location ||

                                '-'
                            }

                        </p>

                    </div>

                </div>

                <div className="mt-6">

                    <label className="font-semibold">

                        Agenda

                    </label>

                    <p className="mt-2 whitespace-pre-wrap">

                        {
                            meeting.agenda ||

                            'No agenda available'
                        }

                    </p>

                </div>

                <div className="mt-6">

                    <label className="font-semibold">

                        Academic Session

                    </label>

                    <p className="mt-2">

                        {
                            meeting.academic_session_name ||

                            '-'
                        }

                    </p>

                </div>

                <div className="mt-8 flex gap-3">

                    <Link
                        to={`/dashboard/associations/association-meetings/edit/${meeting.id}`}
                        className="px-4 py-2 bg-yellow-500 text-white rounded"
                    >
                        Edit
                    </Link>

                    <Link
                        to="/dashboard/associations/association-meetings"
                        className="px-4 py-2 bg-gray-500 text-white rounded"
                    >
                        Back to List
                    </Link>

                </div>

            </div>

        </div>
    );
};

export default AssociationMeetingDetailPage;