import { useEffect, useState } from 'react';
import {
    useNavigate,
    useParams,
} from 'react-router-dom';

import AssociationMemberForm from '../components/AssociationMemberForm';
import associationMemberService from '../services/associationMemberService';

const AssociationMemberEditPage = () => {

    const { id } = useParams();

    const navigate =
        useNavigate();

    const [member, setMember] =
        useState(null);

    useEffect(() => {

        loadMember();

    }, []);

    const loadMember = async () => {

        const response =
            await associationMemberService.getById(
                id
            );

        setMember(
            response.data.data
        );
    };

    const handleSubmit = async (
        data
    ) => {

        await associationMemberService.update(
            id,
            data
        );

        navigate(
            '/dashboard/associations/association_members'
        );
    };

    if (!member)
        return <div>Loading...</div>;

    return (
        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">
                Edit Member
            </h1>

            <AssociationMemberForm
                initialData={member}
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AssociationMemberEditPage;