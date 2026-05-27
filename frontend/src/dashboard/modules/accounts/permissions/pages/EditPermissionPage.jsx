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

            // ==============================
            // FLATTEN MODULES
            // ==============================

            const flattenedModules =
                flattenModules(data);

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
            // SORT MODULES
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
                "UPDATE PERMISSION PAYLOAD:",
                payload
            );

            // ==============================
            // UPDATE
            // ==============================

            await PermissionService.updatePermission(

                id,

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
                "Update Permission Error:",
                error
            );

            console.log(
                error.response?.data
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