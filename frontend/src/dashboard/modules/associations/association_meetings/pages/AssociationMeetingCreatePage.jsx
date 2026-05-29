// ============================================
// IMPORTS
// ============================================

import { useNavigate } from 'react-router-dom';

import AssociationMeetingForm from '../components/AssociationMeetingForm';

import associationMeetingService from '../services/associationMeetingService';

// ============================================
// COMPONENT
// ============================================

const AssociationMeetingCreatePage = () => {

    const navigate = useNavigate();

    const handleSubmit = async (
        data
    ) => {

        try {

            await associationMeetingService.create(
                data
            );

            navigate(
                '/dashboard/associations/association-meetings'
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">
                Create Association Meeting
            </h1>

            <AssociationMeetingForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AssociationMeetingCreatePage;