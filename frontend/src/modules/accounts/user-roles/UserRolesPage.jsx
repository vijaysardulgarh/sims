import {
    useEffect,
    useState
} from "react";

import {
    useParams
} from "react-router-dom";

import roleService
from "../../services/roleService";

import userService
from "../../services/userService";


const UserRolesPage = () => {

    // =====================================
    // PARAMS
    // =====================================

    const {
        id
    } = useParams();


    // =====================================
    // STATE
    // =====================================

    const [loading,
        setLoading] =
        useState(false);

    const [roles,
        setRoles] =
        useState([]);

    const [selectedRoles,
        setSelectedRoles] =
        useState([]);


    // =====================================
    // FETCH
    // =====================================

    useEffect(() => {

        fetchData();

    }, []);


    const fetchData =
        async () => {

        try {

            setLoading(true);

            // =============================
            // GET ALL ROLES
            // =============================

            const rolesData =
                await roleService.getRoles();

            setRoles(rolesData);

            // =============================
            // GET USER
            // =============================

            const userData =
                await userService.getUser(
                    id
                );

            setSelectedRoles(

                userData.roles || []
            );

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // TOGGLE ROLE
    // =====================================

    const toggleRole =
        (roleCode) => {

        if (

            selectedRoles.includes(
                roleCode
            )

        ) {

            setSelectedRoles(

                selectedRoles.filter(

                    item =>
                        item !== roleCode
                )
            );

        } else {

            setSelectedRoles([

                ...selectedRoles,

                roleCode,
            ]);
        }
    };


    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit =
        async (e) => {

        e.preventDefault();

        try {

            setLoading(true);

            await userService.assignRoles(

                id,

                selectedRoles
            );

            alert(
                "Roles updated successfully"
            );

        } catch (error) {

            console.error(error);

            alert(
                "Failed to update roles"
            );

        } finally {

            setLoading(false);
        }
    };


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

                <h1
                    className="
                        text-3xl
                        font-bold
                        text-gray-800
                    "
                >

                    User Roles

                </h1>

                <p
                    className="
                        text-gray-500
                        mt-1
                    "
                >

                    Assign roles to this user

                </p>

            </div>


            {/* ================================= */}
            {/* FORM */}
            {/* ================================= */}

            <form
                onSubmit={handleSubmit}
                className="space-y-4"
            >

                {

                    roles.map((role) => (

                        <label

                            key={role.id}

                            className="
                                flex
                                items-center
                                gap-4
                                border
                                rounded-xl
                                px-4
                                py-4
                                hover:bg-gray-50
                                cursor-pointer
                            "
                        >

                            <input

                                type="checkbox"

                                checked={

                                    selectedRoles.includes(
                                        role.code
                                    )
                                }

                                onChange={() =>

                                    toggleRole(
                                        role.code
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

                                    {role.name}

                                </p>

                                <p
                                    className="
                                        text-sm
                                        text-gray-500
                                    "
                                >

                                    {role.code}

                                </p>

                            </div>

                        </label>
                    ))
                }


                {/* ================================= */}
                {/* SUBMIT */}
                {/* ================================= */}

                <div className="flex justify-end pt-4">

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
                                : "Save Roles"
                        }

                    </button>

                </div>

            </form>

        </div>
    );
};


export default UserRolesPage;