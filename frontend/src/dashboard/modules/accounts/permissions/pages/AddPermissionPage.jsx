import {

    useEffect,

    useState

} from "react";

import {

    useNavigate

} from "react-router-dom";

import PermissionForm from "../components/PermissionForm";

import PermissionService from "../services/permissionService";

import * as ModuleService from "../../modules/services/moduleService";


const AddPermissionPage = () => {

    const navigate = useNavigate();

    // =====================================
    // STATE
    // =====================================

    const [modules, setModules] = useState([]);

    const [loading, setLoading] = useState(false);


    // =====================================
    // LOAD MODULES
    // =====================================

    useEffect(() => {

        loadModules();

    }, []);


    const loadModules = async () => {

        try {

            const response = await ModuleService.getModules();

            setModules(response);

        } catch (error) {

            console.error(
                "Load Modules Error:",
                error
            );
        }
    };


    // =====================================
    // CREATE PERMISSION
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            setLoading(true);

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

        } finally {

            setLoading(false);
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

                modules={modules}

                loading={loading}

                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AddPermissionPage;