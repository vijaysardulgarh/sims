import {
    useEffect,
    useState
} from "react";

import {
    Link
} from "react-router-dom";

import PermissionService from "../services/permissionService";


const PermissionsListPage = () => {

    // =====================================
    // STATE
    // =====================================

    const [permissions, setPermissions] =
        useState([]);


    // =====================================
    // FETCH PERMISSIONS
    // =====================================

    useEffect(() => {

        fetchPermissions();

    }, []);


    const fetchPermissions = async () => {

        try {

            const data =
                await PermissionService.getPermissions();

            setPermissions(data);

        } catch (error) {

            console.error(
                "Fetch Permissions Error:",
                error
            );
        }
    };


    // =====================================
    // DELETE PERMISSION
    // =====================================

    const handleDelete = async (
        id
    ) => {

        const confirmDelete = window.confirm(

            "Delete permission?"
        );

        if (!confirmDelete) return;

        try {

            await PermissionService.deletePermission(
                id
            );

            fetchPermissions();

        } catch (error) {

            console.error(
                "Delete Permission Error:",
                error
            );
        }
    };


    return (

        <div className="p-4">

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div className="flex justify-between items-center mb-6">

                <h1 className="text-2xl font-bold">

                    Permissions

                </h1>

                <Link
                    to="/dashboard/permissions/add"
                    className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
                >

                    Add Permission

                </Link>

            </div>


            {/* ================================= */}
            {/* TABLE */}
            {/* ================================= */}

            <div className="overflow-x-auto bg-white rounded shadow">

                <table className="w-full border-collapse">

                    <thead>

                        <tr className="bg-gray-100">

                            <th className="border p-3 text-left">
                                ID
                            </th>

                            <th className="border p-3 text-left">
                                Name
                            </th>

                            <th className="border p-3 text-left">
                                Code
                            </th>

                            <th className="border p-3 text-left">
                                Module
                            </th>

                            <th className="border p-3 text-center">
                                Actions
                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        {
                            permissions.length > 0 ? (

                                permissions.map((item) => (

                                    <tr
                                        key={item.id}
                                        className="hover:bg-gray-50"
                                    >

                                        <td className="border p-3">

                                            {item.id}

                                        </td>

                                        <td className="border p-3">

                                            {item.name}

                                        </td>

                                        <td className="border p-3">

                                            {item.code}

                                        </td>

                                        <td className="border p-3">

                                            {item.module}

                                        </td>

                                        <td className="border p-3">

                                            <div className="flex gap-2 justify-center">

                                                <Link
                                                    to={`/dashboard/permissions/edit/${item.id}`}
                                                    className="bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded"
                                                >

                                                    Edit

                                                </Link>

                                                <button
                                                    onClick={() =>
                                                        handleDelete(item.id)
                                                    }
                                                    className="bg-red-600 hover:bg-red-700 text-white px-3 py-1 rounded"
                                                >

                                                    Delete

                                                </button>

                                            </div>

                                        </td>

                                    </tr>
                                ))

                            ) : (

                                <tr>

                                    <td
                                        colSpan="5"
                                        className="border p-4 text-center text-gray-500"
                                    >

                                        No Permissions Found

                                    </td>

                                </tr>
                            )
                        }

                    </tbody>

                </table>

            </div>

        </div>
    );
};

export default PermissionsListPage;