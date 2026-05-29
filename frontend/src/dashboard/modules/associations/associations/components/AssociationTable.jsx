import { Link } from 'react-router-dom';

const AssociationTable = ({
    associations = [],
    onDelete,
}) => {

    if (!Array.isArray(associations)) {

        return (
            <div>
                Invalid association data
            </div>
        );
    }

    return (

        <div className="overflow-x-auto bg-white rounded-2xl shadow">

            <table className="w-full">

                <thead className="bg-gray-100">

                    <tr>

                        <th className="text-left p-4">
                            Name
                        </th>

                        <th className="text-left p-4">
                            Type
                        </th>

                        <th className="text-left p-4">
                            Status
                        </th>

                        <th className="text-left p-4">
                            Chairperson
                        </th>

                        <th className="text-left p-4">
                            Actions
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                        associations.map((item) => (

                            <tr
                                key={item.id}
                                className="border-t"
                            >

                                <td className="p-4">
                                    {item.name}
                                </td>

                                <td className="p-4">
                                    {item.association_type}
                                </td>

                                <td className="p-4">
                                    {item.status}
                                </td>

                                <td className="p-4">
                                    {item.chairperson_name || '-'}
                                </td>

                                <td className="p-4 flex gap-3">

                                    <Link
                                        to={`/dashboard/associations/associations/${item.id}`}
                                        className="text-blue-600"
                                    >
                                        View
                                    </Link>

                                    <Link
                                        to={`/dashboard/associations/associations/edit/${item.id}`}
                                        className="text-green-600"
                                    >
                                        Edit
                                    </Link>

                                    <button
                                        onClick={() =>
                                            onDelete(item.id)
                                        }
                                        className="text-red-600"
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

export default AssociationTable;