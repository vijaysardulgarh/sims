import {
    useParams,
    Link
} from "react-router-dom";

import {
    ShieldCheck,
    ArrowLeft
} from "lucide-react";

import RolePermissionsForm from
"../components/RolePermissionForm";


const RolePermissionsPage = () => {

    // =====================================
    // PARAMS
    // =====================================

    const {
        id
    } = useParams();


    return (

        <div
            className="
                min-h-screen
                bg-gray-50
                p-6
            "
        >

            {/* ================================= */}
            {/* PAGE CONTAINER */}
            {/* ================================= */}

            <div
                className="
                    max-w-7xl
                    mx-auto
                    space-y-6
                "
            >

                {/* ================================= */}
                {/* TOP BAR */}
                {/* ================================= */}

                <div
                    className="
                        flex
                        items-center
                        justify-between
                        flex-wrap
                        gap-4
                    "
                >

                    {/* LEFT */}

                    <div
                        className="
                            flex
                            items-center
                            gap-4
                        "
                    >

                        {/* ICON */}

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


                        {/* TITLE */}

                        <div>

                            <h1
                                className="
                                    text-3xl
                                    font-bold
                                    text-gray-900
                                "
                            >

                                Role Permissions

                            </h1>

                            <p
                                className="
                                    text-gray-500
                                    mt-1
                                "
                            >

                                Configure access control
                                and assign permissions
                                to this role.

                            </p>

                        </div>

                    </div>


                    {/* RIGHT */}

                    <Link
                        to="/dashboard/roles"
                        className="
                            inline-flex
                            items-center
                            gap-2
                            px-4
                            py-2.5
                            rounded-xl
                            border
                            border-gray-300
                            bg-white
                            text-gray-700
                            hover:bg-gray-100
                            transition
                            duration-200
                            shadow-sm
                        "
                    >

                        <ArrowLeft
                            className="
                                w-4
                                h-4
                            "
                        />

                        Back To Roles

                    </Link>

                </div>


                {/* ================================= */}
                {/* ROLE INFO CARD */}
                {/* ================================= */}

                <div
                    className="
                        bg-white
                        rounded-2xl
                        shadow-sm
                        border
                        border-gray-200
                        p-6
                    "
                >

                    <div
                        className="
                            flex
                            items-center
                            justify-between
                            flex-wrap
                            gap-4
                        "
                    >

                        {/* LEFT */}

                        <div>

                            <p
                                className="
                                    text-sm
                                    font-medium
                                    text-gray-500
                                    uppercase
                                    tracking-wide
                                "
                            >

                                Role ID

                            </p>

                            <h2
                                className="
                                    text-2xl
                                    font-bold
                                    text-gray-900
                                    mt-1
                                "
                            >

                                #{id}

                            </h2>

                        </div>


                        {/* RIGHT */}

                        <div
                            className="
                                flex
                                items-center
                                gap-3
                                px-4
                                py-3
                                rounded-xl
                                bg-blue-50
                                border
                                border-blue-100
                            "
                        >

                            <ShieldCheck
                                className="
                                    w-5
                                    h-5
                                    text-blue-600
                                "
                            />

                            <div>

                                <p
                                    className="
                                        text-sm
                                        font-semibold
                                        text-blue-700
                                    "
                                >

                                    Access Control

                                </p>

                                <p
                                    className="
                                        text-xs
                                        text-blue-500
                                    "
                                >

                                    Manage role-based
                                    permissions securely

                                </p>

                            </div>

                        </div>

                    </div>

                </div>


                {/* ================================= */}
                {/* ROLE PERMISSIONS FORM */}
                {/* ================================= */}

                <div
                    className="
                        bg-white
                        rounded-2xl
                        shadow-sm
                        border
                        border-gray-200
                        p-6
                    "
                >

                    <RolePermissionsForm
                        roleId={id}
                    />

                </div>

            </div>

        </div>
    );
};


export default RolePermissionsPage;