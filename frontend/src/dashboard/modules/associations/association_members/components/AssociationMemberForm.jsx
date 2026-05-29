import { useState } from 'react';

const AssociationMemberForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] =
        useState({

            association:
                initialData.association || '',

            staff:
                initialData.staff || '',

            designation:
                initialData.designation || '',

            email:
                initialData.email || '',

            phone_number:
                initialData.phone_number || '',
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

        <form
            onSubmit={handleSubmit}
            className="space-y-4 bg-white p-6 rounded shadow"
        >

            <input
                type="number"
                name="association"
                placeholder="Association ID"
                value={formData.association}
                onChange={handleChange}
                className="w-full border p-2"
                required
            />

            <input
                type="number"
                name="staff"
                placeholder="Staff ID"
                value={formData.staff}
                onChange={handleChange}
                className="w-full border p-2"
                required
            />

            <input
                type="text"
                name="designation"
                placeholder="Designation"
                value={formData.designation}
                onChange={handleChange}
                className="w-full border p-2"
                required
            />

            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                className="w-full border p-2"
            />

            <input
                type="text"
                name="phone_number"
                placeholder="Phone Number"
                value={formData.phone_number}
                onChange={handleChange}
                className="w-full border p-2"
            />

            <button
                type="submit"
                className="px-4 py-2 bg-blue-600 text-white rounded"
            >
                Save
            </button>

        </form>
    );
};

export default AssociationMemberForm;