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

import driverService from "../services/driverService";


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

    const [driver, setDriver] =
        useState(null);

    const [loading, setLoading] =
        useState(false);

    // ======================
    // LOAD DRIVER
    // ======================

    useEffect(() => {

        loadDriver();

    }, []);

    const loadDriver = async () => {

        try {

            const response =
                await driverService.getDriver(id);

            setDriver(response);

        } catch (error) {

            toast.error(
                "Failed to load driver"
            );
        }
    };

    // ======================
    // UPDATE DRIVER
    // ======================

    const handleSubmit = async (data) => {

        try {

            setLoading(true);

            await driverService.updateDriver(
                id,
                data
            );

            toast.success(
                "Driver updated successfully"
            );

            navigate(
                "/dashboard/transport/drivers"
            );

        } catch (error) {

            toast.error(
                "Failed to update driver"
            );

        } finally {

            setLoading(false);
        }
    };

    // ======================
    // LOADING
    // ======================

    if (!driver) {

        return (
            <div>
                Loading driver...
            </div>
        );
    }

    return (

        <div className="space-y-6">

            <h1 className="text-2xl font-bold">

                Edit Driver

            </h1>

            <Form
                initialData={driver}
                onSubmit={handleSubmit}
                loading={loading}
            />

        </div>
    );
};

export default Edit;