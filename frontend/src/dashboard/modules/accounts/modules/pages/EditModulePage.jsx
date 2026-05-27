// src/modules/accounts/modules/pages/ModuleEditPage.jsx

import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import ModuleForm from "../components/ModuleForm";

import {
    getModule,
    getModules,
    updateModule,
} from "../services/moduleService";


export default function ModuleEditPage() {

    const navigate = useNavigate();

    const { id } = useParams();

    // =====================================
    // FORM STATE
    // =====================================

    const [formData, setFormData] = useState({

        parent: "",

        name: "",

        slug: "",

        path: "",

        icon: "",

        order: 0,

        is_menu: true,

        is_active: true,
    });

    // =====================================
    // PARENT MODULES
    // =====================================

    const [parentModules, setParentModules] = useState([]);

    // =====================================
    // LOAD DATA
    // =====================================

    useEffect(() => {

        loadModule();

        loadParentModules();

    }, []);

    // =====================================
    // LOAD MODULE
    // =====================================

    const loadModule = async () => {

        try {

            const data = await getModule(id);

            setFormData({

                parent: data.parent || "",

                name: data.name || "",

                slug: data.slug || "",

                path: data.path || "",

                icon: data.icon || "",

                order: data.order || 0,

                is_menu: data.is_menu ?? true,

                is_active: data.is_active ?? true,
            });

        } catch (error) {

            console.error(error);
        }
    };

    // =====================================
    // LOAD PARENT MODULES
    // =====================================

    const loadParentModules = async () => {

        try {

            const data = await getModules();

            // =================================
            // REMOVE CURRENT MODULE
            // TO PREVENT SELF PARENTING
            // =================================

            const filteredModules = data.filter(
                (module) =>
                    module.id !== Number(id)
            );

            setParentModules(
                filteredModules
            );

        } catch (error) {

            console.error(error);
        }
    };

    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked,
        } = e.target;

        // =================================
        // AUTO GENERATE SLUG
        // =================================

        if (name === "name") {

            setFormData({

                ...formData,

                name: value,

                slug: value
                    .toLowerCase()
                    .trim()
                    .replaceAll(" ", "-"),
            });

            return;
        }

        // =================================
        // NORMAL UPDATE
        // =================================

        setFormData({

            ...formData,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        });
    };

    // =====================================
    // HANDLE SUBMIT
    // =====================================

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            // =================================
            // PREPARE PAYLOAD
            // =================================

            const payload = {

                ...formData,

                parent:
                    formData.parent === ""
                        ? null
                        : Number(formData.parent),

                order: Number(formData.order),

                path:
                    formData.path?.trim() || null,

                icon:
                    formData.icon?.trim() || null,
            };

            console.log(
                "UPDATE PAYLOAD:",
                payload
            );

            // =================================
            // UPDATE MODULE
            // =================================

            await updateModule(
                id,
                payload
            );

            // =================================
            // REDIRECT
            // =================================

            navigate(
                "/dashboard/modules"
            );

        } catch (error) {

            console.error(error);

            console.log(
                error.response?.data
            );
        }
    };

    return (

        <div className="p-6">

            {/* HEADER */}

            <div className="mb-6">

                <h1 className="text-2xl font-bold">

                    Edit Module

                </h1>

            </div>

            {/* FORM CARD */}

            <div className="bg-white rounded-xl shadow p-6">

                <ModuleForm

                    formData={formData}

                    handleChange={handleChange}

                    handleSubmit={handleSubmit}

                    isEdit={true}

                    parentModules={parentModules}
                />

            </div>

        </div>
    );
}