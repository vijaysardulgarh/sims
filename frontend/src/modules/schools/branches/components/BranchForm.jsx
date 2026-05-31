import { useState } from "react";

const BranchForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] =
        useState({

            school:
                initialData.school || "",

            name:
                initialData.name || "",

            code:
                initialData.code || "",

            address:
                initialData.address || "",

            city:
                initialData.city || "",

            state:
                initialData.state || "",

            pincode:
                initialData.pincode || "",

            phone:
                initialData.phone || "",

            email:
                initialData.email || "",

            principal_name:
                initialData.principal_name || "",

            is_head_office:
                initialData.is_head_office || false,
        });

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked,
        } = e.target;

        setFormData({

            ...formData,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        });
    };

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);
    };

    return (

        <form onSubmit={handleSubmit}>

            <input
                type="number"
                name="school"
                placeholder="School ID"
                value={formData.school}
                onChange={handleChange}
            />

            <input
                type="text"
                name="name"
                placeholder="Branch Name"
                value={formData.name}
                onChange={handleChange}
            />

            <input
                type="text"
                name="code"
                placeholder="Branch Code"
                value={formData.code}
                onChange={handleChange}
            />

            <textarea
                name="address"
                placeholder="Address"
                value={formData.address}
                onChange={handleChange}
            />

            <input
                type="text"
                name="city"
                placeholder="City"
                value={formData.city}
                onChange={handleChange}
            />

            <input
                type="text"
                name="state"
                placeholder="State"
                value={formData.state}
                onChange={handleChange}
            />

            <input
                type="text"
                name="pincode"
                placeholder="Pincode"
                value={formData.pincode}
                onChange={handleChange}
            />

            <input
                type="text"
                name="phone"
                placeholder="Phone"
                value={formData.phone}
                onChange={handleChange}
            />

            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
            />

            <input
                type="text"
                name="principal_name"
                placeholder="Principal Name"
                value={formData.principal_name}
                onChange={handleChange}
            />

            <label>

                Head Office

                <input
                    type="checkbox"
                    name="is_head_office"
                    checked={
                        formData.is_head_office
                    }
                    onChange={handleChange}
                />

            </label>

            <button type="submit">

                Save

            </button>

        </form>
    );
};

export default BranchForm;