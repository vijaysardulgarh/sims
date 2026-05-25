// src/modules/accounts/modules/pages/ModuleAddPage.jsx

import {
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import ModuleForm from "../components/ModuleForm";

import {
    createModule,
} from "../services/moduleService";


export default function ModuleAddPage() {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({

        name: "",
        slug: "",
        description: "",
        is_active: true,
    });

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked,
        } = e.target;

        setFormData({

            ...formData,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        });
    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            await createModule(
                formData
            );

            navigate(
                "/dashboard/modules"
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (

        <div className="p-6">

            <div className="mb-6">

                <h1 className="text-2xl font-bold">

                    Add Module

                </h1>

            </div>

            <div className="bg-white rounded-xl shadow p-6">

                <ModuleForm
                    formData={formData}
                    handleChange={handleChange}
                    handleSubmit={handleSubmit}
                    isEdit={false}
                />

            </div>

        </div>
    );
}