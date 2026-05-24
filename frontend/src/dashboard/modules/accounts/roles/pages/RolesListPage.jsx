import {

    useEffect,

    useState

} from "react";

import {

    Link

} from "react-router-dom";

import roleService from "../../services/roleService";


const RolesListPage = () => {

    const [roles, setRoles] = useState([]);

    const [loading, setLoading] = useState(true);


    // =====================================
    // FETCH ROLES
    // =====================================

    useEffect(() => {

        fetchRoles();

    }, []);


    const fetchRoles = async () => {

        try {

            const data = await roleService.getRoles();

            setRoles(data.results || data);

        } catch (error) {

            console.error(
                "Fetch Roles Error:",
                error
            );

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // DELETE ROLE
    // =====================================

    const handleDelete = async (
        id
    ) => {

        const confirmDelete = window.confirm(

            "Are you sure you want to delete this role?"
        );

        if (!confirmDelete) return;

        try {

            await roleService.deleteRole(id);

            fetchRoles();

        } catch (error) {

            console.error(
                "Delete Role Error:",
                error
            );
        }
    };


    if (loading) {

        return <p>Loading...</p>;
    }


    return (

        <div className="p-4">

            {/* HEADER */}

            <div className="flex justify-between items-center mb-4">

                <h1 className="text-2xl font-bold">

                    Roles List

                </h1>

                <Link

                    to="/dashboard/roles/add"

                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >

                    Add Role

                </Link>

            </div>


            {/* TABLE */}

            <table className="w-full border">

                <thead>

                    <tr className="bg-gray-100">

                        <th className="border p-2">
                            ID
                        </th>

                        <th className="border p-2">
                            Name
                        </th>

                        <th className="border p-2">
                            Code
                        </th>

                        <th className="border p-2">
                            Active
                        </th>

                        <th className="border p-2">
                            Actions
                        </th>

                    </tr>

                </thead>


                <tbody>

                    {
                        roles.map((role) => (

                            <tr key={role.id}>

                                <td className="border p-2">

                                    {role.id}

                                </td>

                                <td className="border p-2">

                                    {role.name}

                                </td>

                                <td className="border p-2">

                                    {role.code}

                                </td>

                                <td className="border p-2">

                                    {
                                        role.is_active
                                            ? "Yes"
                                            : "No"
                                    }

                                </td>

                                <td className="border p-2 flex gap-2">

                                    {/* EDIT */}

                                    <Link

                                        to={`/dashboard/roles/edit/${role.id}`}

                                        className="bg-yellow-500 text-white px-3 py-1 rounded"
                                    >

                                        Edit

                                    </Link>


                                    {/* DELETE */}

                                    <button

                                        onClick={() =>
                                            handleDelete(role.id)
                                        }

                                        className="bg-red-600 text-white px-3 py-1 rounded"
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

export default RolesListPage;