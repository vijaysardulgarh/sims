import {
    useEffect,
    useState,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import toast from "react-hot-toast";

import Form from "../components/Form";

import transportRouteService from "../services/transportRouteService";


const Edit = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [route, setRoute] =
        useState(null);

    const [loading, setLoading] =
        useState(false);

    useEffect(() => {

        loadRoute();

    }, []);

    const loadRoute = async () => {

        try {

            const response =
                await transportRouteService.getRoute(id);

            setRoute(response);

        } catch (error) {

            toast.error(
                "Failed to load route"
            );
        }
    };

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await transportRouteService.updateRoute(
                id,
                data
            );

            toast.success(
                "Route updated successfully"
            );

            navigate(
                "/dashboard/transport/transport-routes"
            );

        } catch (error) {

            toast.error(
                "Failed to update route"
            );

        } finally {

            setLoading(false);
        }
    };

    if (!route) {

        return (
            <div>
                Loading route...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Edit Route

            </h1>

            <Form
                initialData={route}
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Edit;