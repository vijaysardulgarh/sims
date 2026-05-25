import {

    useEffect,

    useState

} from "react";

import {

    useNavigate,

    useParams

} from "react-router-dom";

import PermissionForm from "../components/PermissionForm";

import PermissionService from "../services/permissionService";

import * as ModuleService from "../../modules/services/moduleService";


const EditPermissionPage = () => {

    // =====================================
    // ROUTER
    // =====================================

    const { id } = useParams();

    const navigate = useNavigate();


    // =====================================
    // STATE
    // =====================================

    const [permission, setPermission] =
        useState(null);

    const [modules, setModules] =
        useState([]);

    const [loading, setLoading] =
        useState(false);


    // =====================================
    // FETCH DATA
    // =====================================

    useEffect(() => {

        fetchPermission();

        fetchModules();

    }, []);


    // =====================================
    // FETCH PERMISSION
    // =====================================

    const fetchPermission = async () => {

        try {

            const data =
                await PermissionService.getPermission(id);

            setPermission(data);

        } catch (error) {

            console.error(
                "Fetch Permission Error:",
                error
            );
        }
    };


    // =====================================
    // FETCH MODULES
    // =====================================

    const fetchModules = async () => {

        try {

            const data =
                await ModuleService.getModules();

            setModules(data);

        } catch (error) {

            console.error(
                "Fetch Modules Error:",
                error
            );
        }
    };


    // =====================================
    // UPDATE PERMISSION
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            setLoading(true);

            await PermissionService.updatePermission(

                id,

                formData
            );

            navigate(
                "/dashboard/permissions"
            );

        } catch (error) {

            console.error(
                "Update Permission Error:",
                error
            );

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // LOADING
    // =====================================

    if (!permission) {

        return (

            <div className="p-4">

                Loading...

            </div>
        );
    }


    return (

        <div className="p-4">

            {/* ================================= */}
            {/* PAGE TITLE */}
            {/* ================================= */}

            <h1 className="text-2xl font-bold mb-6">

                Edit Permission

            </h1>


            {/* ================================= */}
            {/* FORM */}
            {/* ================================= */}

            <PermissionForm

                initialData={permission}

                modules={modules}

                onSubmit={handleSubmit}

                loading={loading}
            />

        </div>
    );
};

export default EditPermissionPage;