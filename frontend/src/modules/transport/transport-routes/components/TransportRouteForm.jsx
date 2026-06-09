import {
    useEffect,
    useState,
} from "react";


const Form = ({
    initialData = {},
    onSubmit,
    loading = false,
}) => {

    const [formData, setFormData] =
        useState({
            route_name: "",
            start_location: "",
            end_location: "",
            vehicle: "",
            driver: "",
        });

    useEffect(() => {

        if (initialData) {

            setFormData({
                route_name:
                    initialData.route_name || "",

                start_location:
                    initialData.start_location || "",

                end_location:
                    initialData.end_location || "",

                vehicle:
                    initialData.vehicle || "",

                driver:
                    initialData.driver || "",
            });
        }

    }, [initialData]);

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);
    };

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            <input
                type="text"
                name="route_name"
                placeholder="Route Name"
                value={formData.route_name}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <input
                type="text"
                name="start_location"
                placeholder="Start Location"
                value={formData.start_location}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <input
                type="text"
                name="end_location"
                placeholder="End Location"
                value={formData.end_location}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <input
                type="number"
                name="vehicle"
                placeholder="Vehicle ID"
                value={formData.vehicle}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <input
                type="number"
                name="driver"
                placeholder="Driver ID"
                value={formData.driver}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <button
                type="submit"
                disabled={loading}
                className="
                    bg-blue-600
                    text-white
                    px-4
                    py-2
                    rounded
                "
            >
                {
                    loading
                        ? "Saving..."
                        : "Save"
                }
            </button>

        </form>
    );
};

export default Form;