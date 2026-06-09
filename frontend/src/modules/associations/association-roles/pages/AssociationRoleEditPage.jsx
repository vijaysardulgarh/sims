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

    const [loading, setLoading] =
        useState(true);

    // ========================================
    // LOAD ROLE
    // ========================================

    useEffect(() => {

        loadRole();

    }, [id]);

    const loadRole = async () => {

        try {

            const response =
                await associationRoleService.getById(
                    id
                );

            console.log(
                'EDIT RESPONSE:',
                response
            );

            setRole(
                response?.data || {}
            );

        }

        catch (error) {

            console.error(
                error
            );

        }

        finally {

            setLoading(
                false
            );

        }

    };

    // ========================================
    // SUBMIT
    // ========================================

    const handleSubmit = async (
        data
    ) => {

        try {

            await associationRoleService.update(
                id,
                data
            );

            navigate(
                '/dashboard/associations/association-roles'
            );

        }

        catch (error) {

            console.error(
                error
            );

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
    // NO DATA
    // ========================================

    if (!role) {

        return (

            <div className="p-6 text-red-600">

                Role not found.

            </div>

        );

    }

    // ========================================
    // UI
    // ========================================

    return (

        <div className="p-6">

            <div className="bg-white p-6 rounded-2xl shadow max-w-3xl">

                <h1 className="text-3xl font-bold mb-6">

                    Edit Association Role

                </h1>

                <AssociationRoleForm

                    initialData={role}

                    onSubmit={handleSubmit}

                />

            </div>

        </div>

    );

};

export default AssociationRoleEditPage;