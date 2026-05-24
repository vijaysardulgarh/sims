import { useNavigate } from "react-router-dom";

import PermissionForm from "../components/PermissionForm";

import PermissionService from "../services/permissionService";


const AddPermissionPage = () => {

    const navigate = useNavigate();


    // =====================================
    // CREATE PERMISSION
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            await PermissionService.createPermission(
                formData
            );

            navigate(
                "/dashboard/permissions"
            );

        } catch (error) {

            console.error(
                "Create Permission Error:",
                error
            );
        }
    };


    return (

        <div className="p-4">

            {/* ================================= */}
            {/* PAGE TITLE */}
            {/* ================================= */}

            <h1 className="text-2xl font-bold mb-6">

                Add Permission

            </h1>


            {/* ================================= */}
            {/* FORM */}
            {/* ================================= */}

            <PermissionForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AddPermissionPage;