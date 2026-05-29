import { useNavigate } from 'react-router-dom';

import AssociationMemberForm from '../components/AssociationMemberForm';
import associationMemberService from '../services/associationMemberService';

const AssociationMemberCreatePage = () => {

    const navigate =
        useNavigate();

    const handleSubmit = async (
        data
    ) => {

        await associationMemberService.create(
            data
        );

        navigate(
            '/dashboard/associations/association_members'
        );
    };

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">
                Create Member
            </h1>

            <AssociationMemberForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AssociationMemberCreatePage;