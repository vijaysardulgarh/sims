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

import vehicleService from "../services/Service";


const Edit = () => {

    // ======================
    // PARAMS
    // ======================

    const { id } = useParams();

    // ======================
    // NAVIGATION
    // ======================

    const navigate = useNavigate();

    // ======================
    // STATES
    // ======================

    const [vehicle, setVehicle] =
        useState(null);

    const [loading, setLoading] =
        useState(false);

    // ======================
    // LOAD VEHICLE
    // ======================

    useEffect(() => {

        loadVehicle();

    }, []);

    const loadVehicle = async () => {

        try {

            const response =
                await vehicleService.getVehicle(id);

            setVehicle(response);

        } catch (error) {

            toast.error(
                "Failed to load vehicle"
            );
        }
    };

    // ======================
    // UPDATE VEHICLE
    // ======================

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await vehicleService.updateVehicle(
                id,
                data
            );

            toast.success(
                "Vehicle updated successfully"
            );

            navigate(
                "/dashboard/transport/vehicles"
            );

        } catch (error) {

            toast.error(
                "Failed to update vehicle"
            );

        } finally {

            setLoading(false);
        }
    };

    // ======================
    // LOADING
    // ======================

    if (!vehicle) {

        return (
            <div>
                Loading vehicle...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Edit Vehicle

            </h1>

            <Form
                initialData={vehicle}
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Edit;