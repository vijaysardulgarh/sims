import { useNavigate } from "react-router-dom";

import RoleForm from "../components/RoleForm";

import roleService from "../../services/roleService";


const AddRolePage = () => {

    const navigate = useNavigate();


    // =====================================
    // CREATE ROLE
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            await roleService.createRole(
                formData
            );

            navigate(
                "/dashboard/roles"
            );

        } catch (error) {

            console.error(
                "Create Role Error:",
                error
            );
        }
    };


    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">

                Add Role

            </h1>

            <RoleForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AddRolePage;