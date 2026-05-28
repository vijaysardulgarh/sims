// src/modules/schools/pages/SchoolEditPage.jsx

import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import SchoolForm from "../components/SchoolForm";

import {
    getSchool,
    updateSchool,
} from "../services/schoolService";

const SchoolEditPage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [school, setSchool] =
        useState(null);

    useEffect(() => {

        const fetchSchool = async () => {

            const data =
                await getSchool(id);

            setSchool(data);
        };

        fetchSchool();

    }, [id]);

    const handleSubmit = async (
        formData
    ) => {

        try {

            await updateSchool(
                id,
                formData
            );

            navigate(
                "/dashboard/schools"
            );

        } catch (error) {

            console.error(error);
        }
    };

    if (!school) {

        return <p>Loading...</p>;
    }

    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">
                Edit School
            </h1>

            <SchoolForm
                initialData={school}
                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default SchoolEditPage;