import {
    useState,
} from "react";

import { useNavigate } from "react-router-dom";

import toast from "react-hot-toast";

import Form from "../components/Form";

import transportRouteService from "../services/transportRouteService";


const Create = () => {

    const navigate = useNavigate();

    const [loading, setLoading] =
        useState(false);

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await transportRouteService.createRoute(
                data
            );

            toast.success(
                "Route created successfully"
            );

            navigate(
                "/dashboard/transport/transport-routes"
            );

        } catch (error) {

            toast.error(
                "Failed to create route"
            );

        } finally {

            setLoading(false);
        }
    };

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Create Route

            </h1>

            <Form
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Create;