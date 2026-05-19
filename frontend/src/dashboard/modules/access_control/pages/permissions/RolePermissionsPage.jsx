import {
    useParams
} from "react-router-dom";

import PermissionsForm
from "../../components/PermissionsForm";


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
                space-y-6
            "
        >

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div>

                <h1
                    className="
                        text-3xl
                        font-bold
                        text-gray-800
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

                    Manage permissions assigned
                    to this role

                </p>

            </div>


            {/* ================================= */}
            {/* FORM */}
            {/* ================================= */}

            <PermissionsForm
                roleId={id}
            />

        </div>
    );
};


export default RolePermissionsPage;