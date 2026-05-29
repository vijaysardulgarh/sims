// ============================================
// IMPORTS
// ============================================

import { Link } from 'react-router-dom';

// ============================================
// COMPONENT
// ============================================

const AssociationMemberTable = ({
    members,
    onDelete,
}) => {

    return (

        <div className="overflow-x-auto bg-white rounded-xl shadow">

            <table className="min-w-full">

                <thead className="bg-gray-100">

                    <tr>

                        <th className="px-4 py-3">
                            ID
                        </th>

                        <th className="px-4 py-3">
                            Association
                        </th>

                        <th className="px-4 py-3">
                            Staff
                        </th>

                        <th className="px-4 py-3">
                            Designation
                        </th>

                        <th className="px-4 py-3">
                            Actions
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                        members?.map((member) => (

                            <tr
                                key={member.id}
                                className="border-t"
                            >

                                <td className="px-4 py-3">
                                    {member.id}
                                </td>

                                <td className="px-4 py-3">
                                    {member.association_name}
                                </td>

                                <td className="px-4 py-3">
                                    {member.staff_name}
                                </td>

                                <td className="px-4 py-3">
                                    {member.designation}
                                </td>

                                <td className="px-4 py-3">

                                    <div className="flex gap-2">

                                        <Link
                                            to={`/dashboard/associations/association_members/${member.id}`}
                                            className="px-3 py-1 bg-green-600 text-white rounded"
                                        >
                                            View
                                        </Link>

                                        <Link
                                            to={`/dashboard/associations/association_members/edit/${member.id}`}
                                            className="px-3 py-1 bg-yellow-500 text-white rounded"
                                        >
                                            Edit
                                        </Link>

                                        <button
                                            onClick={() =>
                                                onDelete(
                                                    member.id
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
                    }

                </tbody>

            </table>

        </div>
    );
};

export default AssociationMemberTable;