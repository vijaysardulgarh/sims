import {
    useEffect,
    useMemo,
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

    const [search, setSearch] =
        useState("");


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
        id,
        isSystemPermission
    ) => {

        // =================================
        // PREVENT SYSTEM DELETE
        // =================================

        if (isSystemPermission) {

            alert(
                "System permissions cannot be deleted."
            );

            return;
        }

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
    // FILTERED PERMISSIONS
    // =====================================

    const filteredPermissions = useMemo(() => {

        return permissions.filter((item) => {

            const keyword =
                search.toLowerCase();

            return (

                item.name?.toLowerCase().includes(keyword) ||

                item.code?.toLowerCase().includes(keyword) ||

                item.module_name?.toLowerCase().includes(keyword)
            );
        });

    }, [permissions, search]);


    // =====================================
    // LOADING
    // =====================================

    if (loading) {

        return (

            <div className="p-6">

                <div className="text-gray-500">

                    Loading permissions...

                </div>

            </div>
        );
    }


    return (

        <div className="p-6">

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h1 className="text-2xl font-bold">

                        Permissions

                    </h1>

                    <p className="text-gray-500 mt-1">

                        Manage system permissions

                    </p>

                </div>

                <Link
                    to="/dashboard/permissions/add"
                    className="
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        px-4
                        py-2
                        rounded-lg
                    "
                >

                    Add Permission

                </Link>

            </div>


            {/* ================================= */}
            {/* SEARCH */}
            {/* ================================= */}

            <div className="mb-5">

                <input
                    type="text"
                    placeholder="Search permissions..."
                    value={search}
                    onChange={(e) =>
                        setSearch(e.target.value)
                    }
                    className="
                        w-full
                        md:w-80
                        border
                        border-gray-300
                        rounded-lg
                        px-4
                        py-2
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                />

            </div>


            {/* ================================= */}
            {/* TABLE */}
            {/* ================================= */}

            <div className="overflow-x-auto bg-white rounded-xl shadow">

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

                            <th className="border p-3 text-left">
                                Action
                            </th>

                            <th className="border p-3 text-left">
                                Status
                            </th>

                            <th className="border p-3 text-left">
                                Type
                            </th>

                            <th className="border p-3 text-center">
                                Actions
                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        {
                            filteredPermissions.length > 0 ? (

                                filteredPermissions.map((item) => (

                                    <tr
                                        key={item.id}
                                        className="hover:bg-gray-50"
                                    >

                                        {/* ID */}

                                        <td className="border p-3">

                                            {item.id}

                                        </td>


                                        {/* NAME */}

                                        <td className="border p-3 font-medium">

                                            {item.name}

                                        </td>


                                        {/* CODE */}

                                        <td className="border p-3">

                                            <span className="
                                                font-mono
                                                text-blue-600
                                            ">

                                                {item.code}

                                            </span>

                                        </td>


                                        {/* MODULE */}

                                        <td className="border p-3">

                                            {item.module_name}

                                        </td>


                                        {/* ACTION */}

                                        <td className="border p-3">

                                            {item.action_display}

                                        </td>


                                        {/* STATUS */}

                                        <td className="border p-3">

                                            {
                                                item.is_active ? (

                                                    <span className="
                                                        bg-green-100
                                                        text-green-700
                                                        px-2
                                                        py-1
                                                        rounded-full
                                                        text-sm
                                                    ">

                                                        Active

                                                    </span>

                                                ) : (

                                                    <span className="
                                                        bg-red-100
                                                        text-red-700
                                                        px-2
                                                        py-1
                                                        rounded-full
                                                        text-sm
                                                    ">

                                                        Inactive

                                                    </span>
                                                )
                                            }

                                        </td>


                                        {/* TYPE */}

                                        <td className="border p-3">

                                            {
                                                item.is_system_permission ? (

                                                    <span className="
                                                        bg-purple-100
                                                        text-purple-700
                                                        px-2
                                                        py-1
                                                        rounded-full
                                                        text-sm
                                                    ">

                                                        System

                                                    </span>

                                                ) : (

                                                    <span className="
                                                        bg-gray-100
                                                        text-gray-700
                                                        px-2
                                                        py-1
                                                        rounded-full
                                                        text-sm
                                                    ">

                                                        Custom

                                                    </span>
                                                )
                                            }

                                        </td>


                                        {/* ACTIONS */}

                                        <td className="border p-3">

                                            <div className="
                                                flex
                                                gap-2
                                                justify-center
                                            ">

                                                {/* EDIT */}

                                                <Link
                                                    to={`/dashboard/permissions/edit/${item.id}`}
                                                    className="
                                                        bg-yellow-500
                                                        hover:bg-yellow-600
                                                        text-white
                                                        px-3
                                                        py-1
                                                        rounded
                                                    "
                                                >

                                                    Edit

                                                </Link>


                                                {/* DELETE */}

                                                <button
                                                    onClick={() =>
                                                        handleDelete(
                                                            item.id,
                                                            item.is_system_permission
                                                        )
                                                    }
                                                    className="
                                                        bg-red-600
                                                        hover:bg-red-700
                                                        text-white
                                                        px-3
                                                        py-1
                                                        rounded
                                                    "
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
                                        colSpan="8"
                                        className="
                                            border
                                            p-6
                                            text-center
                                            text-gray-500
                                        "
                                    >

                                        No permissions found

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