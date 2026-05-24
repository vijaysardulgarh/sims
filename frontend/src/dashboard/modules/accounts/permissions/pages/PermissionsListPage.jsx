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

    const [loading, setLoading] =
        useState(true);


    // =====================================
    // FETCH PERMISSIONS
    // =====================================

    useEffect(() => {

        fetchPermissions();

    }, []);


    const fetchPermissions = async () => {

        try {

            setLoading(true);

            const data =
                await PermissionService.getPermissions();


            // =================================
            // DEBUG RESPONSE
            // =================================

            console.log(

                "PERMISSIONS RESPONSE:",

                data
            );


            // =================================
            // SAFE DATA HANDLING
            // =================================

            if (Array.isArray(data)) {

                setPermissions(data);

            }

            else if (

                Array.isArray(data?.results)

            ) {

                setPermissions(
                    data.results
                );

            }

            else if (

                Array.isArray(data?.data)

            ) {

                setPermissions(
                    data.data
                );

            }

            else {

                setPermissions([]);
            }
        }

        catch (error) {

            console.error(

                "Fetch Permissions Error:",

                error
            );

            setPermissions([]);
        }

        finally {

            setLoading(false);
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
        }

        catch (error) {

            console.error(

                "Delete Permission Error:",

                error
            );
        }
    };


    // =====================================
    // LOADING
    // =====================================

    if (loading) {

        return (

            <div className="p-4">

                Loading permissions...

            </div>
        );
    }


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
                            permissions?.length > 0 ? (

                                permissions.map((item) => (

                                    <tr
                                        key={item.id}
                                        className="hover:bg-gray-50"
                                    >

                                        {/* ID */}

                                        <td className="border p-3">

                                            {item.id}

                                        </td>


                                        {/* NAME */}

                                        <td className="border p-3">

                                            {item.name}

                                        </td>


                                        {/* CODE */}

                                        <td className="border p-3">

                                            {item.code}

                                        </td>


                                        {/* MODULE */}

                                        <td className="border p-3">

                                            {item.module}

                                        </td>


                                        {/* ACTIONS */}

                                        <td className="border p-3">

                                            <div className="flex gap-2 justify-center">

                                                {/* EDIT */}

                                                <Link
                                                    to={`/dashboard/permissions/edit/${item.id}`}
                                                    className="bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded"
                                                >

                                                    Edit

                                                </Link>


                                                {/* DELETE */}

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