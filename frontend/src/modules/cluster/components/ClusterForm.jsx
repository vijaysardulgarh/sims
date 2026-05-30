// src/modules/clusters/components/ClusterForm.jsx

import { useState } from "react";

const ClusterForm = ({
    initialData = {},
    onSubmit,
    loading,
}) => {

    const [formData, setFormData] =
        useState({

            name:
                initialData.name || "",

            code:
                initialData.code || "",

            description:
                initialData.description || "",

            email:
                initialData.email || "",

            phone:
                initialData.phone || "",

            address:
                initialData.address || "",

            timezone:
                initialData.timezone ||
                "Asia/Kolkata",

            currency:
                initialData.currency ||
                "INR",

            latitude:
                initialData.latitude || "",

            longitude:
                initialData.longitude || "",

            geo_radius_meters:
                initialData.geo_radius_meters ||
                100,

            logo: null,
        });

    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange = (e) => {

        const {
            name,
            value,
            files,
        } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]:
                files
                    ? files[0]
                    : value,
        }));
    };

    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit = (e) => {

        e.preventDefault();

        const payload =
            new FormData();

        Object.entries(formData).forEach(

            ([key, value]) => {

                if (

                    value !== null &&
                    value !== undefined &&
                    value !== ""

                ) {

                    payload.append(
                        key,
                        value
                    );
                }
            }
        );

        onSubmit(payload);
    };

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            <input
                type="text"
                name="name"
                placeholder="Cluster Name"
                value={formData.name}
                onChange={handleChange}
                className="border p-2 w-full"
                required
            />

            <input
                type="text"
                name="code"
                placeholder="Cluster Code"
                value={formData.code}
                onChange={handleChange}
                className="border p-2 w-full"
                required
            />

            <textarea
                name="description"
                placeholder="Description"
                value={
                    formData.description
                }
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="text"
                name="phone"
                placeholder="Phone"
                value={formData.phone}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <textarea
                name="address"
                placeholder="Address"
                value={formData.address}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="text"
                name="timezone"
                placeholder="Timezone"
                value={formData.timezone}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="text"
                name="currency"
                placeholder="Currency"
                value={formData.currency}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="number"
                step="0.000001"
                name="latitude"
                placeholder="Latitude"
                value={formData.latitude}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="number"
                step="0.000001"
                name="longitude"
                placeholder="Longitude"
                value={formData.longitude}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="number"
                name="geo_radius_meters"
                placeholder="Geo Radius"
                value={
                    formData.geo_radius_meters
                }
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <input
                type="file"
                name="logo"
                accept="image/*"
                onChange={handleChange}
                className="border p-2 w-full"
            />

            <button
                type="submit"
                disabled={loading}
                className="bg-blue-500 text-white px-4 py-2 rounded"
            >

                {
                    loading
                        ? "Saving..."
                        : "Save Cluster"
                }

            </button>

        </form>
    );
};

export default ClusterForm;