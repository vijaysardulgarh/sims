// ============================================
// IMPORTS
// ============================================

import {
    useEffect,
    useState,
} from 'react';

import {
    useNavigate,
    useParams,
} from 'react-router-dom';

import AssociationMeetingForm from '../components/AssociationMeetingForm';

import associationMeetingService from '../services/associationMeetingService';

// ============================================
// COMPONENT
// ============================================

const AssociationMeetingEditPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [meeting, setMeeting] =
        useState(null);

    useEffect(() => {

        fetchMeeting();

    }, [id]);

    const fetchMeeting = async () => {

        const response =
            await associationMeetingService.getById(
                id
            );

        setMeeting(
            response.data
        );
    };

    const handleSubmit = async (
        data
    ) => {

        await associationMeetingService.update(
            id,
            data
        );

        navigate(
            '/dashboard/associations/association-meetings'
        );
    };

    if (!meeting)
        return <div>Loading...</div>;

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">
                Edit Association Meeting
            </h1>

            <AssociationMeetingForm
                initialData={meeting}
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AssociationMeetingEditPage;