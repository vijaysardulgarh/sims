import {
    useEffect,
    useState
} from "react";

import permissionService from "../services/permissionService";

import roleService from "../services/roleService";


const PermissionsForm = ({

    roleId,

    onSuccess,

}) => {

    // =====================================
    // STATE
    // =====================================

    const [loading,
        setLoading] =
        useState(false);

    const [permissions,
        setPermissions] =
        useState([]);

    const [selectedPermissions,
        setSelectedPermissions] =
        useState([]);

    const [role,
        setRole] =
        useState(null);


    // =====================================
    // LOAD DATA
    // =====================================

    useEffect(() => {

        fetchData();

    }, [roleId]);


    // =====================================
    // FETCH
    // =====================================

    const fetchData =
        async () => {

        try {

            setLoading(true);

            // =============================
            // GET ROLE
            // =============================

            const roleData =
                await roleService.getRole(
                    roleId
                );

            setRole(roleData);

            // =============================
            // GET ALL PERMISSIONS
            // =============================

            const permissionsData =
                await permissionService.getPermissions();

            setPermissions(
                permissionsData
            );

            // =============================
            // SET SELECTED
            // =============================

            setSelectedPermissions(

                roleData.permissions || []
            );

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // TOGGLE PERMISSION
    // =====================================

    const togglePermission =
        (permissionCode) => {

        if (

            selectedPermissions.includes(
                permissionCode
            )

        ) {

            setSelectedPermissions(

                selectedPermissions.filter(

                    item =>
                        item !== permissionCode
                )
            );

        } else {

            setSelectedPermissions([

                ...selectedPermissions,

                permissionCode,
            ]);
        }
    };


    // =====================================
    // GROUP BY MODULE
    // =====================================

    const groupedPermissions =
        permissions.reduce(

            (acc, permission) => {

                const module =
                    permission.module ||
                    "General";

                if (!acc[module]) {

                    acc[module] = [];
                }

                acc[module].push(
                    permission
                );

                return acc;

            },

            {}
        );


    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit =
        async (e) => {

        e.preventDefault();

        try {

            setLoading(true);

            await permissionService.assignPermissionsToRole(

                roleId,

                selectedPermissions
            );

            alert(
                "Permissions updated successfully"
            );

            if (onSuccess) {

                onSuccess();
            }

        } catch (error) {

            console.error(error);

            alert(
                "Failed to update permissions"
            );

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // LOADING
    // =====================================

    if (loading && !role) {

        return (

            <div>

                Loading...

            </div>
        );
    }


    return (

        <div
            className="
                bg-white
                rounded-2xl
                shadow-sm
                p-6
            "
        >

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div className="mb-6">

                <h2
                    className="
                        text-2xl
                        font-bold
                        text-gray-800
                    "
                >

                    Role Permissions

                </h2>

                <p
                    className="
                        text-gray-500
                        mt-1
                    "
                >

                    {role?.name}

                </p>

            </div>


            {/* ================================= */}
            {/* FORM */}
            {/* ================================= */}

            <form
                onSubmit={handleSubmit}
                className="space-y-8"
            >

                {

                    Object.entries(
                        groupedPermissions
                    ).map(

                        ([module,
                            modulePermissions]) => (

                            <div
                                key={module}
                                className="
                                    border
                                    rounded-2xl
                                    overflow-hidden
                                "
                            >

                                {/* MODULE HEADER */}

                                <div
                                    className="
                                        bg-gray-100
                                        px-5
                                        py-4
                                        border-b
                                    "
                                >

                                    <h3
                                        className="
                                            font-semibold
                                            text-lg
                                            text-gray-700
                                        "
                                    >

                                        {module}

                                    </h3>

                                </div>


                                {/* PERMISSIONS */}

                                <div
                                    className="
                                        grid
                                        grid-cols-1
                                        md:grid-cols-2
                                        xl:grid-cols-3
                                        gap-4
                                        p-5
                                    "
                                >

                                    {

                                        modulePermissions.map(

                                            (permission) => (

                                                <label

                                                    key={permission.id}

                                                    className="
                                                        flex
                                                        items-center
                                                        gap-3
                                                        border
                                                        rounded-xl
                                                        px-4
                                                        py-3
                                                        hover:bg-gray-50
                                                        cursor-pointer
                                                    "
                                                >

                                                    <input

                                                        type="checkbox"

                                                        checked={

                                                            selectedPermissions.includes(

                                                                permission.code
                                                            )
                                                        }

                                                        onChange={() =>

                                                            togglePermission(

                                                                permission.code
                                                            )
                                                        }
                                                    />

                                                    <div>

                                                        <p
                                                            className="
                                                                font-medium
                                                                text-gray-700
                                                            "
                                                        >

                                                            {permission.name}

                                                        </p>

                                                        <p
                                                            className="
                                                                text-sm
                                                                text-gray-500
                                                            "
                                                        >

                                                            {permission.code}

                                                        </p>

                                                    </div>

                                                </label>
                                            )
                                        )
                                    }

                                </div>

                            </div>
                        )
                    )
                }


                {/* ================================= */}
                {/* SUBMIT */}
                {/* ================================= */}

                <div className="flex justify-end">

                    <button

                        type="submit"

                        disabled={loading}

                        className="
                            bg-blue-600
                            hover:bg-blue-700
                            text-white
                            px-6
                            py-3
                            rounded-xl
                            font-medium
                            transition
                        "
                    >

                        {
                            loading
                                ? "Saving..."
                                : "Save Permissions"
                        }

                    </button>

                </div>

            </form>

        </div>
    );
};


export default PermissionsForm;