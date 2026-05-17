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
            name: "",
            code: "",
            email: "",
            phone: "",
        });

    useEffect(() => {

        setFormData({
            name: initialData.name || "",
            code: initialData.code || "",
            email: initialData.email || "",
            phone: initialData.phone || "",
        });

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
                name="name"
                placeholder="School Name"
                value={formData.name}
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
                name="code"
                placeholder="School Code"
                value={formData.code}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
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
                name="phone"
                placeholder="Phone"
                value={formData.phone}
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