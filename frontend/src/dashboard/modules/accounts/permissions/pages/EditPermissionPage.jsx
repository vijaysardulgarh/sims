import {

    useEffect,

    useState

} from "react";

import {

    useNavigate,

    useParams

} from "react-router-dom";

import AccessControlForm from "../permissions/forms/PermissionsForm";

import accessControlService from "../permissions/services/permissionService";


const EditAccessControlPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [accessControl, setAccessControl] =
        useState(null);


    // =====================================
    // FETCH
    // =====================================

    useEffect(() => {

        fetchAccessControl();

    }, []);


    const fetchAccessControl = async () => {

        try {

            const data =
                await accessControlService.getAccessControl(id);

            setAccessControl(data);

        } catch (error) {

            console.error(
                "Fetch Access Control Error:",
                error
            );
        }
    };


    // =====================================
    // UPDATE
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            await accessControlService.updateAccessControl(

                id,

                formData
            );

            navigate(
                "/dashboard/access-controls"
            );

        } catch (error) {

            console.error(
                "Update Access Control Error:",
                error
            );
        }
    };


    if (!accessControl) {

        return <p>Loading...</p>;
    }


    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">

                Edit Access Control

            </h1>

            <AccessControlForm

                initialData={accessControl}

                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default EditAccessControlPage;