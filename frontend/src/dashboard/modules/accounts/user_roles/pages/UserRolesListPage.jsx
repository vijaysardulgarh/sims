import {

    useEffect,

    useState

} from "react";

import {

    Link

} from "react-router-dom";

import userRoleService from "../../services/userRoleService";


const UserRolesListPage = () => {

    const [userRoles, setUserRoles] =
        useState([]);


    // =====================================
    // FETCH
    // =====================================

    useEffect(() => {

        fetchUserRoles();

    }, []);


    const fetchUserRoles = async () => {

        try {

            const data =
                await userRoleService.getUserRoles();

            setUserRoles(data);

        } catch (error) {

            console.error(error);
        }
    };


    // =====================================
    // DELETE
    // =====================================

    const handleDelete = async (
        id
    ) => {

        const confirmDelete = window.confirm(

            "Delete user role?"
        );

        if (!confirmDelete) return;

        try {

            await userRoleService.deleteUserRole(id);

            fetchUserRoles();

        } catch (error) {

            console.error(error);
        }
    };


    return (

        <div className="p-4">

            {/* HEADER */}

            <div className="flex justify-between mb-4">

                <h1 className="text-2xl font-bold">

                    User Roles

                </h1>

                <Link
                    to="/dashboard/user-roles/add"
                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >

                    Add User Role

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
                            User
                        </th>

                        <th className="border p-2">
                            Role
                        </th>

                        <th className="border p-2">
                            Actions
                        </th>

                    </tr>

                </thead>


                <tbody>

                    {
                        userRoles.map((item) => (

                            <tr key={item.id}>

                                <td className="border p-2">

                                    {item.id}

                                </td>

                                <td className="border p-2">

                                    {item.user_email}

                                </td>

                                <td className="border p-2">

                                    {item.role_name}

                                </td>

                                <td className="border p-2 flex gap-2">

                                    <Link
                                        to={`/dashboard/user-roles/edit/${item.id}`}
                                        className="bg-yellow-500 text-white px-3 py-1 rounded"
                                    >

                                        Edit

                                    </Link>

                                    <button
                                        onClick={() =>
                                            handleDelete(item.id)
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

export default UserRolesListPage;