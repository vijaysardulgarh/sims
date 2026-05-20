import {
    useEffect,
    useState
} from "react";

import {
    Link
} from "react-router-dom";

import permissionService from "../../services/permissionService";


const PermissionsListPage = () => {

    // =====================================
    // STATE
    // =====================================

    const [permissions,
        setPermissions] =
        useState([]);

    const [loading,
        setLoading] =
        useState(true);


    // =====================================
    // FETCH PERMISSIONS
    // =====================================

    useEffect(() => {

        const token =
            localStorage.getItem(
                "access"
            );

        // =================================
        // WAIT FOR TOKEN
        // =================================

        if (token) {

            fetchPermissions();

        } else {

            setLoading(false);
        }

    }, []);


    const fetchPermissions =
        async () => {

        try {

            const data =
            await permissionService.getPermissions();
        
            console.log(
                "PERMISSIONS:",
                data
            );
            
            setPermissions(
            
                Array.isArray(data)
            
                    ? data
            
                    : []
            );

        } catch (error) {

            console.error(
                "PERMISSION ERROR:",
                error
            );

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // DELETE
    // =====================================

    const handleDelete =
        async (id) => {

        const confirmDelete =
            window.confirm(

                "Delete permission?"
            );

        if (!confirmDelete) {

            return;
        }

        try {

            await permissionService.deletePermission(
                id
            );

            fetchPermissions();

        } catch (error) {

            console.error(
                error
            );
        }
    };


    // =====================================
    // LOADING
    // =====================================

    if (loading) {

        return (

            <div
                className="
                    flex
                    items-center
                    justify-center
                    h-screen
                    text-xl
                "
            >

                Loading permissions...

            </div>
        );
    }


    // =====================================
    // UI
    // =====================================

    return (

        <div
            className="
                bg-white
                rounded-2xl
                shadow-sm
                p-6
            "
        >

            {/* HEADER */}

            <div
                className="
                    flex
                    items-center
                    justify-between
                    mb-6
                "
            >

                <h1
                    className="
                        text-3xl
                        font-bold
                    "
                >

                    Permissions

                </h1>


                <Link

                    to="/dashboard/permissions/add"

                    className="
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        px-5
                        py-3
                        rounded-xl
                    "
                >

                    Add Permission

                </Link>

            </div>


            {/* TABLE */}

            <div
                className="
                    overflow-x-auto
                "
            >

                <table
                    className="
                        w-full
                        border-collapse
                    "
                >

                    <thead>

                        <tr
                            className="
                                bg-gray-100
                            "
                        >

                            <th
                                className="
                                    text-left
                                    p-4
                                "
                            >

                                Name

                            </th>

                            <th
                                className="
                                    text-left
                                    p-4
                                "
                            >

                                Code

                            </th>

                            <th
                                className="
                                    text-left
                                    p-4
                                "
                            >

                                Module

                            </th>

                            <th
                                className="
                                    text-left
                                    p-4
                                "
                            >

                                Active

                            </th>

                            <th
                                className="
                                    text-left
                                    p-4
                                "
                            >

                                Actions

                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        {

Array.isArray(permissions) && permissions.map(

                                (permission) => (

                                    <tr
                                        key={permission.id}
                                        className="
                                            border-b
                                        "
                                    >

                                        <td
                                            className="
                                                p-4
                                            "
                                        >

                                            {permission.name}

                                        </td>

                                        <td
                                            className="
                                                p-4
                                            "
                                        >

                                            {permission.code}

                                        </td>

                                        <td
                                            className="
                                                p-4
                                            "
                                        >

                                            {permission.module}

                                        </td>

                                        <td
                                            className="
                                                p-4
                                            "
                                        >

                                            {

                                                permission.is_active

                                                    ? "Yes"

                                                    : "No"
                                            }

                                        </td>

                                        <td
                                            className="
                                                p-4
                                                flex
                                                gap-3
                                            "
                                        >

                                            <Link

                                                to={`/dashboard/permissions/edit/${permission.id}`}

                                                className="
                                                    text-blue-600
                                                "
                                            >

                                                Edit

                                            </Link>


                                            <button

                                                onClick={() =>
                                                    handleDelete(
                                                        permission.id
                                                    )
                                                }

                                                className="
                                                    text-red-600
                                                "
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


export default PermissionsListPage;