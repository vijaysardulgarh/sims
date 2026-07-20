// src/modules/clusters/components/ClusterForm.jsx

import {
    useEffect,
    useState,
} from "react";

const ClusterForm = ({
    initialData = {},
    onSubmit,
    loading = false,
}) => {

    const [formData, setFormData] = useState({

        // Basic Information
        name: "",
        code: "",
        description: "",

        // CRC Information
        crc_name: "",
        crc_designation: "",
        crc_phone: "",
        crc_email: "",

        // Office Contact
        email: "",
        phone: "",
        address: "",

        // Status
        is_active: true,

    });

    // =====================================
    // Populate form when editing
    // =====================================

    useEffect(() => {

        if (!initialData || Object.keys(initialData).length === 0) {
            return;
        }

        setFormData({

            name: initialData.name || "",

            code: initialData.code || "",

            description: initialData.description || "",

            crc_name: initialData.crc_name || "",

            crc_designation:
                initialData.crc_designation || "",

            crc_phone:
                initialData.crc_phone || "",

            crc_email:
                initialData.crc_email || "",

            email:
                initialData.email || "",

            phone:
                initialData.phone || "",

            address:
                initialData.address || "",

            is_active:
                initialData.is_active ?? true,

        });

    }, [initialData]);

    // =====================================
    // Handle Change
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
    // Submit
    // =====================================

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);

    };

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-6"
        >

            {/* Basic Information */}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

                <div>
                    <label className="block mb-1 font-medium">
                        Cluster Name
                    </label>

                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        className="w-full border rounded-lg p-2"
                        required
                    />
                </div>

                <div>
                    <label className="block mb-1 font-medium">
                        Cluster Code
                    </label>

                    <input
                        type="text"
                        name="code"
                        value={formData.code}
                        onChange={handleChange}
                        className="w-full border rounded-lg p-2"
                        required
                    />
                </div>

            </div>

            <div>

                <label className="block mb-1 font-medium">
                    Description
                </label>

                <textarea
                    name="description"
                    rows="3"
                    value={formData.description}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-2"
                />

            </div>

            {/* CRC Information */}

            <h3 className="text-lg font-semibold border-b pb-2">
                CRC Information
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

                <input
                    type="text"
                    name="crc_name"
                    placeholder="CRC Name"
                    value={formData.crc_name}
                    onChange={handleChange}
                    className="border rounded-lg p-2"
                />

                <input
                    type="text"
                    name="crc_designation"
                    placeholder="CRC Designation"
                    value={formData.crc_designation}
                    onChange={handleChange}
                    className="border rounded-lg p-2"
                />

                <input
                    type="text"
                    name="crc_phone"
                    placeholder="CRC Phone"
                    value={formData.crc_phone}
                    onChange={handleChange}
                    className="border rounded-lg p-2"
                />

                <input
                    type="email"
                    name="crc_email"
                    placeholder="CRC Email"
                    value={formData.crc_email}
                    onChange={handleChange}
                    className="border rounded-lg p-2"
                />

            </div>

            {/* Office Contact */}

            <h3 className="text-lg font-semibold border-b pb-2">
                Office Contact
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

                <input
                    type="email"
                    name="email"
                    placeholder="Office Email"
                    value={formData.email}
                    onChange={handleChange}
                    className="border rounded-lg p-2"
                />

                <input
                    type="text"
                    name="phone"
                    placeholder="Office Phone"
                    value={formData.phone}
                    onChange={handleChange}
                    className="border rounded-lg p-2"
                />

            </div>

            <textarea
                name="address"
                placeholder="Office Address"
                rows="3"
                value={formData.address}
                onChange={handleChange}
                className="w-full border rounded-lg p-2"
            />

            {/* Status */}

            <label className="flex items-center gap-2">

                <input
                    type="checkbox"
                    name="is_active"
                    checked={formData.is_active}
                    onChange={handleChange}
                />

                Active

            </label>

            {/* Buttons */}

            <div className="flex justify-end">

                <button
                    type="submit"
                    disabled={loading}
                    className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
                >

                    {loading
                        ? "Saving..."
                        : "Save Cluster"}

                </button>

            </div>

        </form>

    );

};

export default ClusterForm;