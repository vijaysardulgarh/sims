// src/modules/accounts/modules/pages/ModuleAddPage.jsx

import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import ModuleForm from "../components/ModuleForm";

import {
    createModule,
    getModules,
} from "../services/moduleService";


export default function ModuleAddPage() {

    const navigate = useNavigate();

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
    // LOAD MODULES
    // =====================================

    useEffect(() => {

        fetchModules();

    }, []);

    const fetchModules = async () => {

        try {

            const data = await getModules();

            setParentModules(data);

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
                "MODULE PAYLOAD:",
                payload
            );

            // =================================
            // CREATE MODULE
            // =================================

            await createModule(
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

                    Add Module

                </h1>

            </div>

            {/* FORM CARD */}

            <div className="bg-white rounded-xl shadow p-6">

                <ModuleForm

                    formData={formData}

                    handleChange={handleChange}

                    handleSubmit={handleSubmit}

                    isEdit={false}

                    parentModules={parentModules}
                />

            </div>

        </div>
    );
}