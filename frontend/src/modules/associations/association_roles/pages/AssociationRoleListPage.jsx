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

import associationRoleService from '../services/associationRoleService';

// ============================================
// COMPONENT
// ============================================

const AssociationRoleListPage = () => {

    const [roles, setRoles] =
        useState([]);

    useEffect(() => {

        fetchRoles();

    }, []);

    const fetchRoles = async () => {

        try {

            const response =
                await associationRoleService.getAll();

            setRoles(
                response?.data?.data || []
            );

        } catch (error) {

            console.error(error);
        }
    };

    const handleDelete = async (id) => {

        if (
            !window.confirm(
                'Delete this role?'
            )
        ) {
            return;
        }

        await associationRoleService.delete(
            id
        );

        fetchRoles();
    };

    return (

        <div className="p-6">

            <div className="flex justify-between mb-6">

                <h1 className="text-2xl font-bold">
                    Association Roles
                </h1>

                <Link
                    to="/dashboard/associations/association-roles/create"
                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >
                    Add Role
                </Link>

            </div>

            <table className="w-full border">

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Association</th>
                        <th>Title</th>
                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {
                        roles.map((role) => (

                            <tr key={role.id}>

                                <td>{role.id}</td>

                                <td>
                                    {role.association_name}
                                </td>

                                <td>
                                    {role.title}
                                </td>

                                <td>

                                    <Link
                                        to={`/dashboard/associations/association-roles/${role.id}`}
                                    >
                                        View
                                    </Link>

                                    {' | '}

                                    <Link
                                        to={`/dashboard/associations/association-roles/edit/${role.id}`}
                                    >
                                        Edit
                                    </Link>

                                    {' | '}

                                    <button
                                        onClick={() =>
                                            handleDelete(
                                                role.id
                                            )
                                        }
                                    >
                                        Delete
                                    </button>

                                </td>

                            </tr>

                        ))
                    }

                </tbody>

            </table>

        </div>
    );
};

export default AssociationRoleListPage;