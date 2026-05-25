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
    updateModule,
} from "../services/moduleService";


export default function ModuleEditPage() {

    const navigate = useNavigate();

    const { id } = useParams();

    const [formData, setFormData] = useState({

        name: "",
        slug: "",
        description: "",
        is_active: true,
    });

    useEffect(() => {

        loadModule();

    }, []);

    const loadModule = async () => {

        try {

            const data = await getModule(id);

            setFormData(data);

        } catch (error) {

            console.error(error);
        }
    };

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

            await updateModule(
                id,
                formData
            );

            navigate(
                "/accounts/modules"
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (

        <div className="p-6">

            <div className="mb-6">

                <h1 className="text-2xl font-bold">

                    Edit Module

                </h1>

            </div>

            <div className="bg-white rounded-xl shadow p-6">

                <ModuleForm
                    formData={formData}
                    handleChange={handleChange}
                    handleSubmit={handleSubmit}
                    isEdit={true}
                />

            </div>

        </div>
    );
}