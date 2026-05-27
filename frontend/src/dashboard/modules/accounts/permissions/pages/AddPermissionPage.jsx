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


    // =====================================
    // FLATTEN MODULES
    // =====================================

    const flattenModules = (
        modules = []
    ) => {

        let result = [];

        modules.forEach((module) => {

            result.push(module);

            if (
                module.children &&
                module.children.length > 0
            ) {

                result = [

                    ...result,

                    ...flattenModules(
                        module.children
                    )
                ];
            }
        });

        return result;
    };


    // =====================================
    // LOAD MODULES
    // =====================================

    const loadModules = async () => {

        try {

            const response =
                await ModuleService.getModules();

            // ==============================
            // FLATTEN MODULES
            // ==============================

            const flattenedModules =
                flattenModules(response);

            // ==============================
            // REMOVE DUPLICATES
            // ==============================

            const uniqueModules = Array.from(

                new Map(

                    flattenedModules.map((module) => [

                        module.id,

                        module
                    ])

                ).values()
            );

            // ==============================
            // FILTER ACTIVE
            // ==============================

            const activeModules =
                uniqueModules.filter(
                    (module) =>
                        module.is_active
                );

            // ==============================
            // SORT BY ORDER + NAME
            // ==============================

            activeModules.sort((a, b) => {

                if (a.order !== b.order) {

                    return a.order - b.order;
                }

                return a.name.localeCompare(
                    b.name
                );
            });

            setModules(
                activeModules
            );

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

            // ==============================
            // PREPARE PAYLOAD
            // ==============================

            const payload = {

                ...formData,

                module: Number(
                    formData.module
                ),
            };

            console.log(
                "PERMISSION PAYLOAD:",
                payload
            );

            // ==============================
            // CREATE
            // ==============================

            await PermissionService.createPermission(
                payload
            );

            // ==============================
            // REDIRECT
            // ==============================

            navigate(
                "/dashboard/permissions"
            );

        } catch (error) {

            console.error(
                "Create Permission Error:",
                error
            );

            console.log(
                error.response?.data
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