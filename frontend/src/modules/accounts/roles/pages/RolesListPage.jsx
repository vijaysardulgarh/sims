import {

    useEffect,

    useState

} from "react";

import {

    Link

} from "react-router-dom";

import roleService from "../services/roleService";


const RolesListPage = () => {

    // =====================================
    // STATE
    // =====================================

    const [roles, setRoles] =
        useState([]);

    const [loading, setLoading] =
        useState(true);


    // =====================================
    // FETCH ROLES
    // =====================================

    useEffect(() => {

        fetchRoles();

    }, []);


    const fetchRoles = async () => {

        try {

            const data =
                await roleService.getRoles();


            // =====================================
            // DEBUG RESPONSE
            // =====================================

            console.log(

                "ROLES API RESPONSE:",

                data
            );


            // =====================================
            // SAFE ARRAY HANDLING
            // =====================================

            setRoles(

                Array.isArray(data)

                    ? data

                    : Array.isArray(data.results)

                        ? data.results

                        : []
            );

        }

        catch (error) {

            console.error(

                "Fetch Roles Error:",

                error
            );

        }

        finally {

            setLoading(false);
        }
    };


    // =====================================
    // DELETE ROLE
    // =====================================

    const handleDelete = async (
        id
    ) => {

        const confirmDelete =
            window.confirm(

                "Are you sure you want to delete this role?"
            );

        if (!confirmDelete) {

            return;
        }

        try {

            await roleService.deleteRole(
                id
            );

            fetchRoles();

        }

        catch (error) {

            console.error(

                "Delete Role Error:",

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

                Loading...

            </div>
        );
    }


    // =====================================
    // UI
    // =====================================

    return (

        <div className="p-6 bg-gray-50 min-h-screen">

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h1 className="text-3xl font-bold text-gray-900">

                        Roles Management

                    </h1>

                    <p className="text-gray-500 mt-1">

                        Manage role-based access control
                        for your organization.

                    </p>

                </div>


                <Link

                    to="/dashboard/roles/add"

                    className="
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        px-5
                        py-2.5
                        rounded-xl
                        shadow-sm
                        transition
                    "
                >

                    Add Role

                </Link>

            </div>


            {/* ================================= */}
            {/* EMPTY STATE */}
            {/* ================================= */}

            {
                roles.length === 0 && (

                    <div
                        className="
                            bg-white
                            border
                            rounded-2xl
                            p-10
                            text-center
                            text-gray-500
                            shadow-sm
                        "
                    >

                        No roles found

                    </div>
                )
            }


            {/* ================================= */}
            {/* TABLE */}
            {/* ================================= */}

            {
                roles.length > 0 && (

                    <div
                        className="
                            bg-white
                            rounded-2xl
                            shadow-sm
                            overflow-hidden
                            border
                        "
                    >

                        <table className="w-full">

                            <thead>

                                <tr className="bg-gray-100 text-gray-700">

                                    <th className="border-b p-4 text-left">

                                        ID

                                    </th>

                                    <th className="border-b p-4 text-left">

                                        Name

                                    </th>

                                    <th className="border-b p-4 text-left">

                                        Code

                                    </th>

                                    <th className="border-b p-4 text-left">

                                        Active

                                    </th>

                                    <th className="border-b p-4 text-left">

                                        Actions

                                    </th>

                                </tr>

                            </thead>


                            <tbody>

                                {
                                    roles.map((role) => (

                                        <tr
                                            key={role.id}
                                            className="
                                                hover:bg-gray-50
                                                transition
                                            "
                                        >

                                            {/* ID */}

                                            <td className="border-b p-4">

                                                #{role.id}

                                            </td>


                                            {/* NAME */}

                                            <td className="border-b p-4 font-medium text-gray-800">

                                                {role.name}

                                            </td>


                                            {/* CODE */}

                                            <td className="border-b p-4 text-gray-600">

                                                {role.code}

                                            </td>


                                            {/* ACTIVE */}

                                            <td className="border-b p-4">

                                                <span
                                                    className={`
                                                        px-3
                                                        py-1
                                                        rounded-full
                                                        text-xs
                                                        font-semibold
                                                        ${
                                                            role.is_active

                                                                ? "bg-green-100 text-green-700"

                                                                : "bg-red-100 text-red-700"
                                                        }
                                                    `}
                                                >

                                                    {
                                                        role.is_active

                                                            ? "Active"

                                                            : "Inactive"
                                                    }

                                                </span>

                                            </td>


                                            {/* ACTIONS */}

                                            <td className="border-b p-4">

                                                <div className="flex items-center gap-2">

                                                    {/* EDIT */}

                                                    <Link

                                                        to={`/dashboard/roles/edit/${role.id}`}

                                                        className="
                                                            bg-yellow-500
                                                            hover:bg-yellow-600
                                                            text-white
                                                            px-3
                                                            py-1.5
                                                            rounded-lg
                                                            transition
                                                        "
                                                    >

                                                        Edit

                                                    </Link>


                                                    {/* PERMISSIONS */}

                                                    <Link

                                                        to={`/dashboard/roles/${role.id}/permissions`}

                                                        className="
                                                            bg-blue-600
                                                            hover:bg-blue-700
                                                            text-white
                                                            px-3
                                                            py-1.5
                                                            rounded-lg
                                                            transition
                                                        "
                                                    >

                                                        Permissions

                                                    </Link>


                                                    {/* DELETE */}

                                                    <button

                                                        onClick={() =>
                                                            handleDelete(role.id)
                                                        }

                                                        className="
                                                            bg-red-600
                                                            hover:bg-red-700
                                                            text-white
                                                            px-3
                                                            py-1.5
                                                            rounded-lg
                                                            transition
                                                        "
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
                )
            }

        </div>
    );
};


export default RolesListPage;