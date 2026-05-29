// ============================================
// IMPORTS
// ============================================

import {
    useNavigate,
} from 'react-router-dom';

import AssociationRoleForm from '../components/AssociationRoleForm';

import associationRoleService from '../services/associationRoleService';

// ============================================
// COMPONENT
// ============================================

const AssociationRoleCreatePage = () => {

    const navigate =
        useNavigate();

    const handleSubmit = async (
        data
    ) => {

        await associationRoleService.create(
            data
        );

        navigate(
            '/dashboard/associations/association-roles'
        );
    };

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-6">
                Create Association Role
            </h1>

            <AssociationRoleForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AssociationRoleCreatePage;