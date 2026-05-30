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

import AssociationRoleForm from '../components/AssociationRoleForm';

import associationRoleService from '../services/associationRoleService';

// ============================================
// COMPONENT
// ============================================

const AssociationRoleEditPage = () => {

    const { id } =
        useParams();

    const navigate =
        useNavigate();

    const [role, setRole] =
        useState(null);

    useEffect(() => {

        loadRole();

    }, []);

    const loadRole = async () => {

        const response =
            await associationRoleService.getById(
                id
            );

        setRole(
            response.data.data
        );
    };

    const handleSubmit = async (
        data
    ) => {

        await associationRoleService.update(
            id,
            data
        );

        navigate(
            '/dashboard/associations/association-roles'
        );
    };

    if (!role)
        return <div>Loading...</div>;

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">
                Edit Association Role
            </h1>

            <AssociationRoleForm
                initialData={role}
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AssociationRoleEditPage;