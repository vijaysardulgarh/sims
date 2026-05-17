import {
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import Form from "../components/Form";

import driverService from "../services/driverService";


const Create = () => {

    // ======================
    // NAVIGATION
    // ======================

    const navigate = useNavigate();

    // ======================
    // LOADING
    // ======================

    const [loading, setLoading] =
        useState(false);

    // ======================
    // CREATE DRIVER
    // ======================

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await driverService.createDriver(
                data
            );

            toast.success(
                "Driver created successfully"
            );

            navigate(
                "/dashboard/transport/drivers"
            );

        } catch (error) {

            toast.error(
                "Failed to create driver"
            );

        } finally {

            setLoading(false);
        }
    };

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Create Driver

            </h1>

            <Form
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Create;