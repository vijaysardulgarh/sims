// src/modules/schools/components/SchoolForm.jsx

import { useState } from "react";

const SchoolForm = ({
    initialData = {},
    onSubmit,
    loading,
}) => {

    const [formData, setFormData] = useState({

        name: initialData.name || "",

        code: initialData.code || "",

        email: initialData.email || "",

        phone: initialData.phone || "",

        address: initialData.address || "",

        city: initialData.city || "",

        state: initialData.state || "",

        country: initialData.country || "India",

        principal_name:
            initialData.principal_name || "",

        board: initialData.board || "",

        school_type:
            initialData.school_type || "",

        logo: null,
    });

    // =====================================================
    // HANDLE CHANGE
    // =====================================================

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

    // =====================================================
    // HANDLE SUBMIT
    // =====================================================

    const handleSubmit = (e) => {

        e.preventDefault();

        const payload =
            new FormData();

        Object.entries(formData).forEach(

            ([key, value]) => {

                // Skip empty values

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

    // =====================================================
    // JSX
    // =====================================================

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            {/* NAME */}

            <input
                type="text"
                name="name"
                placeholder="School Name"
                value={formData.name}
                onChange={handleChange}
                className="border p-2 w-full"
                required
            />

            {/* CODE */}

            <input
                type="text"
                name="code"
                placeholder="School Code"
                value={formData.code}
                onChange={handleChange}
                className="border p-2 w-full"
                required
            />

            {/* EMAIL */}

            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* PHONE */}

            <input
                type="text"
                name="phone"
                placeholder="Phone"
                value={formData.phone}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* ADDRESS */}

            <textarea
                name="address"
                placeholder="Address"
                value={formData.address}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* CITY */}

            <input
                type="text"
                name="city"
                placeholder="City"
                value={formData.city}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* STATE */}

            <input
                type="text"
                name="state"
                placeholder="State"
                value={formData.state}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* COUNTRY */}

            <input
                type="text"
                name="country"
                placeholder="Country"
                value={formData.country}
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* PRINCIPAL */}

            <input
                type="text"
                name="principal_name"
                placeholder="Principal Name"
                value={
                    formData.principal_name
                }
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* BOARD */}

            <select
                name="board"
                value={formData.board}
                onChange={handleChange}
                className="border p-2 w-full"
            >

                <option value="">
                    Select Board
                </option>

                <option value="CBSE">
                    CBSE
                </option>

                <option value="ICSE">
                    ICSE
                </option>

                <option value="STATE">
                    STATE
                </option>

                <option value="IB">
                    IB
                </option>

                <option value="CAMBRIDGE">
                    CAMBRIDGE
                </option>

                <option value="OTHER">
                    OTHER
                </option>

            </select>

            {/* SCHOOL TYPE */}

            <select
                name="school_type"
                value={formData.school_type}
                onChange={handleChange}
                className="border p-2 w-full"
            >

                <option value="">
                    Select School Type
                </option>

                <option value="PRIMARY">
                    PRIMARY
                </option>

                <option value="MIDDLE">
                    MIDDLE
                </option>

                <option value="SECONDARY">
                    SECONDARY
                </option>

                <option value="SENIOR_SECONDARY">
                    SENIOR SECONDARY
                </option>

                <option value="K12">
                    K12
                </option>

                <option value="COLLEGE">
                    COLLEGE
                </option>

                <option value="COACHING">
                    COACHING
                </option>

            </select>

            {/* LOGO */}

            <input
                type="file"
                name="logo"
                accept="image/*"
                onChange={handleChange}
                className="border p-2 w-full"
            />

            {/* SUBMIT BUTTON */}

            <button
                type="submit"
                disabled={loading}
                className="bg-blue-500 text-white px-4 py-2 rounded"
            >

                {
                    loading
                        ? "Saving..."
                        : "Save School"
                }

            </button>

        </form>
    );
};

export default SchoolForm;