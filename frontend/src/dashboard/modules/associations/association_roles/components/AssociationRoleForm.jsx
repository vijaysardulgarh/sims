// ============================================
// IMPORTS
// ============================================

import {
    useState,
} from 'react';

// ============================================
// COMPONENT
// ============================================

const AssociationRoleForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] =
        useState({

            association:
                initialData.association || '',

            title:
                initialData.title || '',

            responsibilities:
                initialData.responsibilities || '',
        });

    // ========================================
    // HANDLE CHANGE
    // ========================================

    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]:
                e.target.value,
        });
    };

    // ========================================
    // HANDLE SUBMIT
    // ========================================

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(
            formData
        );
    };

    // ========================================
    // RENDER
    // ========================================

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4 bg-white p-6 rounded-xl shadow"
        >

            {/* ================================= */}
            {/* ASSOCIATION */}
            {/* ================================= */}

            <div>

                <label className="block mb-2 font-medium">

                    Association ID

                </label>

                <input
                    type="number"
                    name="association"
                    value={formData.association}
                    onChange={handleChange}
                    placeholder="Enter Association ID"
                    className="w-full border rounded-lg px-3 py-2"
                    required
                />

            </div>

            {/* ================================= */}
            {/* TITLE */}
            {/* ================================= */}

            <div>

                <label className="block mb-2 font-medium">

                    Role Title

                </label>

                <input
                    type="text"
                    name="title"
                    value={formData.title}
                    onChange={handleChange}
                    placeholder="Enter Role Title"
                    className="w-full border rounded-lg px-3 py-2"
                    required
                />

            </div>

            {/* ================================= */}
            {/* RESPONSIBILITIES */}
            {/* ================================= */}

            <div>

                <label className="block mb-2 font-medium">

                    Responsibilities

                </label>

                <textarea
                    name="responsibilities"
                    value={
                        formData.responsibilities
                    }
                    onChange={handleChange}
                    rows="5"
                    placeholder="Enter Responsibilities"
                    className="w-full border rounded-lg px-3 py-2"
                />

            </div>

            {/* ================================= */}
            {/* BUTTONS */}
            {/* ================================= */}

            <div className="flex gap-3">

                <button
                    type="submit"
                    className="bg-blue-600 text-white px-4 py-2 rounded-lg"
                >
                    Save
                </button>

            </div>

        </form>
    );
};

export default AssociationRoleForm;