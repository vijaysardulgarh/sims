// =========================================
// FILE:
// frontend/src/modules/accounts/user_permissions/pages/UserPermissionsPage.jsx
// =========================================

import {
    useEffect,
    useState
} from "react";

import userPermissionsService from
"../services/userPermissionsService";


const UserPermissionsPage = () => {

    // =====================================
    // STATES
    // =====================================

    const [
        users,
        setUsers
    ] = useState([]);

    const [
        loading,
        setLoading
    ] = useState(true);

    const [
        search,
        setSearch
    ] = useState("");


    // =====================================
    // FETCH
    // =====================================

    useEffect(() => {

        fetchUserPermissions();

    }, []);


    // =====================================
    // FETCH USER PERMISSIONS
    // =====================================

    const fetchUserPermissions = async () => {

        try {

            setLoading(true);

            const response = await (

                userPermissionsService
                .getUserPermissions()
            );

            setUsers(response);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // FILTERED USERS
    // =====================================

    const filteredUsers = users.filter(

        (user) => (

            user.full_name
                ?.toLowerCase()
                .includes(
                    search.toLowerCase()
                )

            ||

            user.email
                ?.toLowerCase()
                .includes(
                    search.toLowerCase()
                )
        )
    );


    // =====================================
    // LOADING
    // =====================================

    if (loading) {

        return (

            <div
                className="
                    p-6
                "
            >

                Loading...

            </div>
        );
    }


    return (

        <div
            className="
                p-6
                space-y-6
            "
        >

            {/* HEADER */}

            <div
                className="
                    flex
                    items-center
                    justify-between
                    gap-4
                    flex-wrap
                "
            >

                <div>

                    <h1
                        className="
                            text-3xl
                            font-bold
                            text-gray-800
                        "
                    >

                        User Permissions

                    </h1>

                    <p
                        className="
                            text-gray-500
                            mt-1
                        "
                    >

                        View effective
                        permissions assigned
                        to users

                    </p>

                </div>


                {/* SEARCH */}

                <input

                    type="text"

                    placeholder="
                        Search user...
                    "

                    value={search}

                    onChange={(e) =>
                        setSearch(
                            e.target.value
                        )
                    }

                    className="
                        border
                        rounded-xl
                        px-4
                        py-2
                        w-72
                        outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                />

            </div>


            {/* TABLE */}

            <div
                className="
                    bg-white
                    rounded-2xl
                    shadow-sm
                    border
                    overflow-hidden
                "
            >

                <div
                    className="
                        overflow-x-auto
                    "
                >

                    <table
                        className="
                            w-full
                            text-sm
                        "
                    >

                        {/* HEAD */}

                        <thead
                            className="
                                bg-gray-50
                                border-b
                            "
                        >

                            <tr>

                                <th
                                    className="
                                        text-left
                                        p-4
                                        font-semibold
                                    "
                                >
                                    User
                                </th>

                                <th
                                    className="
                                        text-left
                                        p-4
                                        font-semibold
                                    "
                                >
                                    Email
                                </th>

                                <th
                                    className="
                                        text-left
                                        p-4
                                        font-semibold
                                    "
                                >
                                    School
                                </th>

                                <th
                                    className="
                                        text-left
                                        p-4
                                        font-semibold
                                    "
                                >
                                    Roles
                                </th>

                                <th
                                    className="
                                        text-left
                                        p-4
                                        font-semibold
                                    "
                                >
                                    Permissions
                                </th>

                            </tr>

                        </thead>


                        {/* BODY */}

                        <tbody>

                            {

                                filteredUsers.length === 0

                                ? (

                                    <tr>

                                        <td
                                            colSpan="5"
                                            className="
                                                text-center
                                                p-10
                                                text-gray-500
                                            "
                                        >

                                            No users found

                                        </td>

                                    </tr>

                                )

                                : (

                                    filteredUsers.map(

                                        (user) => (

                                            <tr

                                                key={user.id}

                                                className="
                                                    border-b
                                                    hover:bg-gray-50
                                                "
                                            >

                                                {/* USER */}

                                                <td
                                                    className="
                                                        p-4
                                                    "
                                                >

                                                    <div
                                                        className="
                                                            font-medium
                                                            text-gray-800
                                                        "
                                                    >

                                                        {
                                                            user.full_name
                                                        }

                                                    </div>

                                                </td>


                                                {/* EMAIL */}

                                                <td
                                                    className="
                                                        p-4
                                                        text-gray-600
                                                    "
                                                >

                                                    {
                                                        user.email
                                                    }

                                                </td>


                                                {/* SCHOOL */}

                                                <td
                                                    className="
                                                        p-4
                                                    "
                                                >

                                                    {

                                                        user.school ||

                                                        "-"
                                                    }

                                                </td>


                                                {/* ROLES */}

                                                <td
                                                    className="
                                                        p-4
                                                    "
                                                >

                                                    <div
                                                        className="
                                                            flex
                                                            flex-wrap
                                                            gap-2
                                                        "
                                                    >

                                                        {

                                                            user.roles.map(

                                                                (
                                                                    role,
                                                                    index
                                                                ) => (

                                                                    <span

                                                                        key={index}

                                                                        className="
                                                                            px-3
                                                                            py-1
                                                                            rounded-full
                                                                            bg-blue-100
                                                                            text-blue-700
                                                                            text-xs
                                                                            font-medium
                                                                        "
                                                                    >

                                                                        {
                                                                            role
                                                                        }

                                                                    </span>
                                                                )
                                                            )
                                                        }

                                                    </div>

                                                </td>


                                                {/* PERMISSIONS */}

                                                <td
                                                    className="
                                                        p-4
                                                    "
                                                >

                                                    <div
                                                        className="
                                                            flex
                                                            flex-wrap
                                                            gap-2
                                                        "
                                                    >

                                                        {

                                                            user.permissions.map(

                                                                (
                                                                    permission,
                                                                    index
                                                                ) => (

                                                                    <span

                                                                        key={index}

                                                                        className="
                                                                            px-3
                                                                            py-1
                                                                            rounded-full
                                                                            bg-green-100
                                                                            text-green-700
                                                                            text-xs
                                                                            font-medium
                                                                        "
                                                                    >

                                                                        {
                                                                            permission
                                                                        }

                                                                    </span>
                                                                )
                                                            )
                                                        }

                                                    </div>

                                                </td>

                                            </tr>
                                        )
                                    )
                                )
                            }

                        </tbody>

                    </table>

                </div>

            </div>

        </div>
    );
};


export default UserPermissionsPage;