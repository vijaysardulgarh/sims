import { useNavigate } from "react-router-dom";

import AccessControlForm from "../forms/AccessControlForm";

import accessControlService from "../services/accessControlService";


const AddAccessControlPage = () => {

    const navigate = useNavigate();


    // =====================================
    // CREATE
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            await accessControlService.createAccessControl(
                formData
            );

            navigate(
                "/dashboard/access-controls"
            );

        } catch (error) {

            console.error(
                "Create Access Control Error:",
                error
            );
        }
    };


    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">

                Add Access Control

            </h1>

            <AccessControlForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AddAccessControlPage;