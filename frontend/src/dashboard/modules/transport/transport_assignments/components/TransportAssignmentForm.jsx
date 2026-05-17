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
            student_name: "",
            route: "",
            stop: "",
            pickup_point: "",
            monthly_fee: "",
            joining_date: "",
        });

    useEffect(() => {

        if (initialData) {

            setFormData({
                student_name:
                    initialData.student_name || "",

                route:
                    initialData.route || "",

                stop:
                    initialData.stop || "",

                pickup_point:
                    initialData.pickup_point || "",

                monthly_fee:
                    initialData.monthly_fee || "",

                joining_date:
                    initialData.joining_date || "",
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
                name="student_name"
                placeholder="Student Name"
                value={formData.student_name}
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
                name="route"
                placeholder="Route ID"
                value={formData.route}
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
                name="stop"
                placeholder="Stop ID"
                value={formData.stop}
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
                name="pickup_point"
                placeholder="Pickup Point"
                value={formData.pickup_point}
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
                name="monthly_fee"
                placeholder="Monthly Fee"
                value={formData.monthly_fee}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <input
                type="date"
                name="joining_date"
                value={formData.joining_date}
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