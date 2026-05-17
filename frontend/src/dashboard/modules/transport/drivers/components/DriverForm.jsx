import {
    useEffect,
    useState,
} from "react";


const Form = ({
    initialData = {},
    onSubmit,
    loading = false,
}) => {

    // ======================
    // FORM STATE
    // ======================

    const [formData, setFormData] =
        useState({
            full_name: "",
            phone: "",
            license_number: "",
            license_expiry: "",
            address: "",
        });

    // ======================
    // LOAD INITIAL DATA
    // ======================

    useEffect(() => {

        if (initialData) {

            setFormData({
                full_name:
                    initialData.full_name || "",

                phone:
                    initialData.phone || "",

                license_number:
                    initialData.license_number || "",

                license_expiry:
                    initialData.license_expiry || "",

                address:
                    initialData.address || "",
            });
        }

    }, [initialData]);

    // ======================
    // HANDLE CHANGE
    // ======================

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    // ======================
    // HANDLE SUBMIT
    // ======================

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
                name="full_name"
                placeholder="Driver Name"
                value={formData.full_name}
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
                placeholder="Phone Number"
                value={formData.phone}
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
                name="license_number"
                placeholder="License Number"
                value={formData.license_number}
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
                name="license_expiry"
                value={formData.license_expiry}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
            />

            <textarea
                name="address"
                placeholder="Address"
                value={formData.address}
                onChange={handleChange}
                className="
                    border
                    rounded
                    p-2
                    w-full
                "
                rows={4}
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