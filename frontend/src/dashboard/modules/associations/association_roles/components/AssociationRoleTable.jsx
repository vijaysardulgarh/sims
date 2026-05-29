// ============================================
// IMPORTS
// ============================================

import {
    Link,
} from 'react-router-dom';

// ============================================
// COMPONENT
// ============================================

const AssociationRoleTable = ({
    roles,
    onDelete,
}) => {

    return (

        <div className="overflow-x-auto bg-white rounded-xl shadow">

            <table className="min-w-full">

                {/* ================================= */}
                {/* HEADER */}
                {/* ================================= */}

                <thead className="bg-gray-100">

                    <tr>

                        <th className="px-4 py-3 text-left">
                            ID
                        </th>

                        <th className="px-4 py-3 text-left">
                            Association
                        </th>

                        <th className="px-4 py-3 text-left">
                            Role Title
                        </th>

                        <th className="px-4 py-3 text-left">
                            Responsibilities
                        </th>

                        <th className="px-4 py-3 text-center">
                            Actions
                        </th>

                    </tr>

                </thead>

                {/* ================================= */}
                {/* BODY */}
                {/* ================================= */}

                <tbody>

                    {
                        roles?.length > 0
                            ? roles.map((role) => (

                                <tr
                                    key={role.id}
                                    className="border-t"
                                >

                                    <td className="px-4 py-3">
                                        {role.id}
                                    </td>

                                    <td className="px-4 py-3">
                                        {
                                            role.association_name
                                        }
                                    </td>

                                    <td className="px-4 py-3">
                                        {role.title}
                                    </td>

                                    <td className="px-4 py-3">

                                        {
                                            role.responsibilities
                                                ?.length > 50
                                                ? `${role.responsibilities.substring(0, 50)}...`
                                                : role.responsibilities
                                        }

                                    </td>

                                    <td className="px-4 py-3">

                                        <div className="flex justify-center gap-2">

                                            {/* VIEW */}

                                            <Link
                                                to={`/dashboard/associations/association-roles/${role.id}`}
                                                className="px-3 py-1 bg-green-600 text-white rounded"
                                            >
                                                View
                                            </Link>

                                            {/* EDIT */}

                                            <Link
                                                to={`/dashboard/associations/association-roles/edit/${role.id}`}
                                                className="px-3 py-1 bg-yellow-500 text-white rounded"
                                            >
                                                Edit
                                            </Link>

                                            {/* DELETE */}

                                            <button
                                                onClick={() =>
                                                    onDelete(
                                                        role.id
                                                    )
                                                }
                                                className="px-3 py-1 bg-red-600 text-white rounded"
                                            >
                                                Delete
                                            </button>

                                        </div>

                                    </td>

                                </tr>

                            ))
                            : (

                                <tr>

                                    <td
                                        colSpan="5"
                                        className="text-center py-6 text-gray-500"
                                    >
                                        No Association Roles Found
                                    </td>

                                </tr>

                            )
                    }

                </tbody>

            </table>

        </div>
    );
};

export default AssociationRoleTable;