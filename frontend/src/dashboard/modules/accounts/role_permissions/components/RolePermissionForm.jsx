import {
    useEffect,
    useState
} from "react";

import {
    ShieldCheck,
    CheckCircle2
} from "lucide-react";

import permissionService from
"../../permissions/services/permissionService";

import roleService from
"../../roles/services/roleService";

import rolePermissionService from
"../services/rolePermissionsService";


const RolePermissionsForm = ({

    roleId,

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
    // FETCH DATA
    // =====================================

    const fetchData =
        async () => {

        try {

            setLoading(true);


            // =================================
            // ROLE
            // =================================

            const roleData =
                await roleService.getRole(
                    roleId
                );

            setRole(roleData);


            // =================================
            // PERMISSIONS
            // =================================

            const permissionsData =
                await permissionService.getPermissions();

            console.log(
                "PERMISSIONS:",
                permissionsData
            );

            setPermissions(

                Array.isArray(
                    permissionsData
                )

                    ? permissionsData

                    : Array.isArray(
                        permissionsData?.results
                    )

                        ? permissionsData.results

                        : []
            );


            // =================================
            // ROLE PERMISSIONS
            // =================================

            const rolePermissionsData =
                await rolePermissionService.getRolePermissions(
                    roleId
                );

            console.log(
                "ROLE PERMISSIONS:",
                rolePermissionsData
            );


            setSelectedPermissions(

                Array.isArray(
                    rolePermissionsData
                )

                    ? rolePermissionsData

                    : []
            );

        } catch (error) {

            console.error(
                "FETCH ERROR:",
                error
            );

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
    // GROUP PERMISSIONS
    // =====================================

    const groupedPermissions =

        Array.isArray(permissions)

            ? permissions.reduce(

                (acc, permission) => {

                    // =========================
                    // MODULE NAME
                    // =========================

                    const module =

                        permission.code
                            ?.split(".")[0]

                            ?.replaceAll("_", " ")

                            || "General";


                    // =========================
                    // CREATE MODULE
                    // =========================

                    if (!acc[module]) {

                        acc[module] = [];
                    }


                    // =========================
                    // PUSH PERMISSION
                    // =========================

                    acc[module].push(
                        permission
                    );

                    return acc;

                },

                {}
            )

            : {};


    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit =
        async (e) => {

        e.preventDefault();

        try {

            setLoading(true);

            console.log(
                "SELECTED:",
                selectedPermissions
            );


            // =================================
            // CLEAN ARRAY
            // =================================

            const cleanedPermissions =

                selectedPermissions.filter(

                    item =>

                        typeof item === "string"
                );

            console.log(
                "CLEANED:",
                cleanedPermissions
            );


            // =================================
            // API CALL
            // =================================

            await rolePermissionService.assignPermissionsToRole(

                roleId,

                cleanedPermissions
            );

            alert(
                "Permissions updated successfully"
            );

        } catch (error) {

            console.error(
                "SUBMIT ERROR:",
                error
            );

            console.log(
                "BACKEND ERROR:",
                error?.response?.data
            );

            alert(

                JSON.stringify(

                    error?.response?.data,

                    null,

                    2
                )
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

            <div className="p-6">

                Loading...

            </div>
        );
    }


    return (

        <div
            className="
                space-y-8
            "
        >

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div
                className="
                    flex
                    items-center
                    justify-between
                    flex-wrap
                    gap-4
                    bg-white
                    border
                    rounded-2xl
                    p-6
                    shadow-sm
                "
            >

                <div
                    className="
                        flex
                        items-center
                        gap-4
                    "
                >

                    <div
                        className="
                            w-14
                            h-14
                            rounded-2xl
                            bg-blue-100
                            flex
                            items-center
                            justify-center
                        "
                    >

                        <ShieldCheck
                            className="
                                w-7
                                h-7
                                text-blue-600
                            "
                        />

                    </div>


                    <div>

                        <h2
                            className="
                                text-2xl
                                font-bold
                                text-gray-900
                            "
                        >

                            {role?.name}

                        </h2>

                        <p
                            className="
                                text-gray-500
                                mt-1
                            "
                        >

                            Configure role-based access
                            permissions.

                        </p>

                    </div>

                </div>


                <div
                    className="
                        bg-blue-50
                        border
                        border-blue-100
                        px-4
                        py-3
                        rounded-xl
                    "
                >

                    <p
                        className="
                            text-sm
                            text-blue-700
                            font-medium
                        "
                    >

                        {
                            selectedPermissions.length
                        } permissions selected

                    </p>

                </div>

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
                                    bg-white
                                    border
                                    border-gray-200
                                    rounded-2xl
                                    shadow-sm
                                    overflow-hidden
                                "
                            >

                                {/* MODULE HEADER */}

                                <div
                                    className="
                                        flex
                                        items-center
                                        justify-between
                                        px-6
                                        py-4
                                        bg-gray-50
                                        border-b
                                    "
                                >

                                    <div>

                                        <h3
                                            className="
                                                text-lg
                                                font-semibold
                                                text-gray-800
                                                capitalize
                                            "
                                        >

                                            {
                                                module.charAt(0)
                                                    .toUpperCase()

                                                +

                                                module.slice(1)
                                            }

                                        </h3>

                                        <p
                                            className="
                                                text-sm
                                                text-gray-500
                                            "
                                        >

                                            {
                                                modulePermissions.length
                                            } permissions

                                        </p>

                                    </div>

                                </div>


                                {/* PERMISSIONS GRID */}

                                <div
                                    className="
                                        p-6
                                        grid
                                        grid-cols-1
                                        md:grid-cols-2
                                        xl:grid-cols-3
                                        gap-4
                                    "
                                >

                                    {
                                        modulePermissions.map(

                                            (permission) => (

                                                <label

                                                    key={permission.id}

                                                    className={`
                                                        flex
                                                        items-start
                                                        gap-4
                                                        p-4
                                                        rounded-2xl
                                                        border
                                                        cursor-pointer
                                                        transition
                                                        hover:border-blue-400
                                                        hover:bg-blue-50

                                                        ${
                                                            selectedPermissions.includes(
                                                                permission.code
                                                            )

                                                                ? "border-blue-500 bg-blue-50"

                                                                : "border-gray-200"
                                                        }
                                                    `}
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

                                                        className="
                                                            mt-1
                                                            w-4
                                                            h-4
                                                            accent-blue-600
                                                        "
                                                    />


                                                    <div
                                                        className="
                                                            flex-1
                                                        "
                                                    >

                                                        <div
                                                            className="
                                                                flex
                                                                items-center
                                                                gap-2
                                                            "
                                                        >

                                                            <h4
                                                                className="
                                                                    font-semibold
                                                                    text-gray-800
                                                                "
                                                            >

                                                                {permission.name}

                                                            </h4>

                                                            {
                                                                selectedPermissions.includes(
                                                                    permission.code
                                                                ) && (

                                                                    <CheckCircle2
                                                                        className="
                                                                            w-4
                                                                            h-4
                                                                            text-blue-600
                                                                        "
                                                                    />
                                                                )
                                                            }

                                                        </div>

                                                        <p
                                                            className="
                                                                text-sm
                                                                text-gray-500
                                                                mt-1
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
                {/* SAVE BUTTON */}
                {/* ================================= */}

                <div
                    className="
                        flex
                        justify-end
                    "
                >

                    <button

                        type="submit"

                        disabled={loading}

                        className="
                            bg-blue-600
                            hover:bg-blue-700
                            disabled:bg-gray-400
                            text-white
                            px-8
                            py-3
                            rounded-2xl
                            font-semibold
                            shadow-sm
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


export default RolePermissionsForm;