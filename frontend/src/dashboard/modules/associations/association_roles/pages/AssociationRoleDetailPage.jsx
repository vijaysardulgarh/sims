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

import associationRoleService from '../services/associationRoleService';

// ============================================
// COMPONENT
// ============================================

const AssociationRoleDetailPage = () => {

    const { id } =
        useParams();

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

    if (!role)
        return <div>Loading...</div>;

    return (

        <div className="p-6">

            <h1 className="text-2xl font-bold mb-4">
                {role.title}
            </h1>

            <p>
                <strong>
                    Association:
                </strong>

                {' '}

                {role.association_name}
            </p>

            <p className="mt-4">

                <strong>
                    Responsibilities:
                </strong>

            </p>

            <p>
                {role.responsibilities}
            </p>

            <Link
                to="/dashboard/associations/association-roles"
                className="inline-block mt-6 bg-gray-600 text-white px-4 py-2 rounded"
            >
                Back
            </Link>

        </div>
    );
};

export default AssociationRoleDetailPage;