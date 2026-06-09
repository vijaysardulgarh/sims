import {
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import Form from "../components/Form";

import vehicleService from "../services/vehicleService";


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
    // CREATE VEHICLE
    // ======================

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await vehicleService.createVehicle(
                data
            );

            toast.success(
                "Vehicle created successfully"
            );

            navigate(
                "/dashboard/transport/vehicles"
            );

        } catch (error) {

            toast.error(
                "Failed to create vehicle"
            );

        } finally {

            setLoading(false);
        }
    };

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Create Vehicle

            </h1>

            <Form
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Create;