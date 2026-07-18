// src/modules/clusters/components/ClusterForm.jsx

import { useState } from "react";

const ClusterForm = ({
    initialData = {},
    onSubmit,
    loading,
}) => {

    const [formData, setFormData] = useState({

        // =====================================
        // BASIC INFORMATION
        // =====================================

        name: initialData.name || "",

        code: initialData.code || "",

        description: initialData.description || "",

        // =====================================
        // CRC INFORMATION
        // =====================================

        crc_name: initialData.crc_name || "",

        crc_designation:
            initialData.crc_designation || "",

        crc_phone:
            initialData.crc_phone || "",

        crc_email:
            initialData.crc_email || "",

        // =====================================
        // OFFICE CONTACT
        // =====================================

        email: initialData.email || "",

        phone: initialData.phone || "",

        address: initialData.address || "",

        // =====================================
        // STATUS
        // =====================================

        is_active:
            initialData.is_active ?? true,

    });

    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked,
        } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,

        }));
    };

    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);
    };

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            {/* ===================================== */}
            {/* BASIC INFORMATION */}
            {/* ===================================== */}

            <input
                type="text"
                name="name"
                placeholder="Cluster Name"
                value={formData.name}
                onChange={handleChange}
                className="border rounded p-2 w-full"
                required
            />

            <input
                type="text"
                name="code"
                placeholder="Cluster Code"
                value={formData.code}
                onChange={handleChange}
                className="border rounded p-2 w-full"
                required
            />

            <textarea
                name="description"
                placeholder="Description"
                value={formData.description}
                onChange={handleChange}
                className="border rounded p-2 w-full"
                rows={3}
            />

            {/* ===================================== */}
            {/* CRC INFORMATION */}
            {/* ===================================== */}

            <input
                type="text"
                name="crc_name"
                placeholder="CRC Name"
                value={formData.crc_name}
                onChange={handleChange}
                className="border rounded p-2 w-full"
                required
            />

            <input
                type="text"
                name="crc_designation"
                placeholder="CRC Designation"
                value={formData.crc_designation}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            <input
                type="text"
                name="crc_phone"
                placeholder="CRC Phone"
                value={formData.crc_phone}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            <input
                type="email"
                name="crc_email"
                placeholder="CRC Email"
                value={formData.crc_email}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            {/* ===================================== */}
            {/* OFFICE CONTACT */}
            {/* ===================================== */}

            <input
                type="email"
                name="email"
                placeholder="Office Email"
                value={formData.email}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            <input
                type="text"
                name="phone"
                placeholder="Office Phone"
                value={formData.phone}
                onChange={handleChange}
                className="border rounded p-2 w-full"
            />

            <textarea
                name="address"
                placeholder="Office Address"
                value={formData.address}
                onChange={handleChange}
                className="border rounded p-2 w-full"
                rows={3}
            />

            {/* ===================================== */}
            {/* STATUS */}
            {/* ===================================== */}

            <label className="flex items-center gap-2">

                <input
                    type="checkbox"
                    name="is_active"
                    checked={formData.is_active}
                    onChange={handleChange}
                />

                Active

            </label>

            {/* ===================================== */}
            {/* SUBMIT */}
            {/* ===================================== */}

            <button
                type="submit"
                disabled={loading}
                className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded"
            >

                {loading ? "Saving..." : "Save Cluster"}

            </button>

        </form>

    );
};

export default ClusterForm;