import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import toast from "react-hot-toast";

import ExtracurricularActivityForm from "../components/ExtracurricularActivityForm";

import extracurricularActivityService from "../services/extracurricularActivityService";

const ExtracurricularActivityEditPage = () => {

    const { id } =
        useParams();

    const navigate =
        useNavigate();

    const [loading, setLoading] =
        useState(false);

    const [initialData, setInitialData] =
        useState({});

    useEffect(() => {

        fetchActivity();

    }, [id]);

    const fetchActivity = async () => {

        try {

            const response =
                await extracurricularActivityService.getById(
                    id
                );

            setInitialData(
                response?.data ||
                response
            );

        } catch (error) {

            console.error(error);

            toast.error(
                "Failed to load activity"
            );
        }
    };

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await extracurricularActivityService.update(
                id,
                data
            );

            toast.success(
                "Activity updated successfully"
            );

            navigate(
                "/dashboard/associations/extracurricular-activities"
            );

        } catch (error) {

            console.error(error);

            toast.error(
                "Update failed"
            );

        } finally {

            setLoading(false);

        }
    };

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Edit Activity

            </h1>

            <ExtracurricularActivityForm

                initialData={initialData}

                onSubmit={handleSubmit}

                loading={loading}

            />

        </div>
    );
};

export default ExtracurricularActivityEditPage;