// src/modules/schools/pages/SchoolCreatePage.jsx

import { useNavigate } from "react-router-dom";

import SchoolForm from "../components/SchoolForm";

import {
    createSchool,
} from "../services/schoolService";

const SchoolCreatePage = () => {

    const navigate = useNavigate();

    const handleSubmit = async (
        formData
    ) => {

        try {

            await createSchool(formData);

            navigate(
                "/dashboard/schools"
            );

        } catch (error) {

            alert(

                JSON.stringify(

                    error.response?.data,

                    null,

                    2
                )
            );

            console.log(

                "Validation Error:",

                error.response?.data
            );
        }
    };

    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">
                Create School
            </h1>

            <SchoolForm
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default SchoolCreatePage;