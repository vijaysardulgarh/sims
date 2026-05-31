import { useState } from "react";

const SchoolForm = ({
    initialData = {},
    onSubmit,
    loading = false
}) => {

    const [formData, setFormData] = useState({

        name: initialData.name || "",

        code: initialData.code || "",

        email: initialData.email || "",

        phone: initialData.phone || "",

        city: initialData.city || "",

        state: initialData.state || "",

        school_type:
            initialData.school_type || "",

        board:
            initialData.board || "",
    });

    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]:
                e.target.value,
        });
    };

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);
    };

    return (

        <form onSubmit={handleSubmit}>

            <input
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="School Name"
            />

            <input
                name="code"
                value={formData.code}
                onChange={handleChange}
                placeholder="School Code"
            />

            <input
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Email"
            />

            <button
                type="submit"
                disabled={loading}
            >
                Save
            </button>

        </form>
    );
};

export default SchoolForm;