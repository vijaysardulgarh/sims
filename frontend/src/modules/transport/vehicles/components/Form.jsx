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
            vehicle_number: "",
            vehicle_type: "",
            registration_number: "",
            capacity: "",
        });

    useEffect(() => {

        if (initialData) {

            setFormData({
                vehicle_number:
                    initialData.vehicle_number || "",

                vehicle_type:
                    initialData.vehicle_type || "",

                registration_number:
                    initialData.registration_number || "",

                capacity:
                    initialData.capacity || "",
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
                name="vehicle_number"
                placeholder="Vehicle Number"
                value={formData.vehicle_number}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            <input
                type="text"
                name="vehicle_type"
                placeholder="Vehicle Type"
                value={formData.vehicle_type}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            <input
                type="text"
                name="registration_number"
                placeholder="Registration Number"
                value={formData.registration_number}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            <input
                type="number"
                name="capacity"
                placeholder="Capacity"
                value={formData.capacity}
                onChange={handleChange}
                className="border rounded p-2 w-full"
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