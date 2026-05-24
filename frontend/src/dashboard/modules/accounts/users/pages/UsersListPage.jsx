import {
    useEffect,
    useState
} from "react";

import {
    Link
} from "react-router-dom";

import userService from "../services/userService";


const UsersListPage = () => {

    const [users,
        setUsers] =
        useState([]);

    const [loading,
        setLoading] =
        useState(true);


    useEffect(() => {

        fetchUsers();

    }, []);


    const fetchUsers =
        async () => {

        try {

            const data =
                await userService.getUsers();

            setUsers(
                Array.isArray(data)
                    ? data
                    : []
            );

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };


    const handleDelete =
        async (id) => {

        const confirmDelete =
            window.confirm(
                "Delete user?"
            );

        if (!confirmDelete) {

            return;
        }

        try {

            await userService.deleteUser(id);

            fetchUsers();

        } catch (error) {

            console.error(error);
        }
    };


    if (loading) {

        return (

            <div className="p-10 text-xl">

                Loading users...

            </div>
        );
    }


    return (

        <div className="bg-white rounded-2xl shadow-sm p-6">

            <div className="flex items-center justify-between mb-6">

                <h1 className="text-3xl font-bold">

                    Users

                </h1>


                <Link
                    to="/dashboard/users/add"
                    className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl"
                >

                    Add User

                </Link>

            </div>


            <div className="overflow-x-auto">

                <table className="w-full border-collapse">

                    <thead>

                        <tr className="bg-gray-100">

                            <th className="text-left p-4">
                                Name
                            </th>

                            <th className="text-left p-4">
                                Email
                            </th>

                            <th className="text-left p-4">
                                Phone
                            </th>

                            <th className="text-left p-4">
                                Active
                            </th>

                            <th className="text-left p-4">
                                Actions
                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        {
                            users.map(

                                (user) => (

                                    <tr
                                        key={user.id}
                                        className="border-b"
                                    >

                                        <td className="p-4">

                                            {user.first_name}

                                            {" "}

                                            {user.last_name}

                                        </td>

                                        <td className="p-4">
                                            {user.email}
                                        </td>

                                        <td className="p-4">
                                            {user.phone}
                                        </td>

                                        <td className="p-4">

                                            {
                                                user.is_active
                                                    ? "Yes"
                                                    : "No"
                                            }

                                        </td>

                                        <td className="p-4 flex gap-3">

                                            <Link
                                                to={`/dashboard/users/profile/${user.id}`}
                                                className="text-green-600"
                                            >
                                                View
                                            </Link>


                                            <Link
                                                to={`/dashboard/users/edit/${user.id}`}
                                                className="text-blue-600"
                                            >
                                                Edit
                                            </Link>


                                            <button
                                                onClick={() =>
                                                    handleDelete(user.id)
                                                }
                                                className="text-red-600"
                                            >
                                                Delete
                                            </button>

                                        </td>

                                    </tr>
                                )
                            )
                        }

                    </tbody>

                </table>

            </div>

        </div>
    );
};


export default UsersListPage;