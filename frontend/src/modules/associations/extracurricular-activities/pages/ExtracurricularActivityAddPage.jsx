import {
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import toast from "react-hot-toast";

import ExtracurricularActivityForm from "../components/ExtracurricularActivityForm";

import extracurricularActivityService from "../services/extracurricularActivityService";

const ExtracurricularActivityAddPage = () => {

    const navigate =
        useNavigate();

    const [loading, setLoading] =
        useState(false);

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await extracurricularActivityService.create(
                data
            );

            toast.success(
                "Activity created successfully"
            );

            navigate(
                "/dashboard/associations/extracurricular-activities"
            );

        } catch (error) {

            console.error(error);

            toast.error(
                "Create failed"
            );

        } finally {

            setLoading(false);

        }
    };

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Add Activity

            </h1>

            <ExtracurricularActivityForm

                onSubmit={handleSubmit}

                loading={loading}

            />

        </div>
    );
};

export default ExtracurricularActivityAddPage;