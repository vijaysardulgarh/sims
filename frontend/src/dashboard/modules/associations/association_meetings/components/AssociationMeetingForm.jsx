// ============================================
// IMPORTS
// ============================================

import { useState } from 'react';

// ============================================
// COMPONENT
// ============================================

const AssociationMeetingForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] =
        useState({

            association:
                initialData.association || '',

            meeting_date:
                initialData.meeting_date || '',

            location:
                initialData.location || '',

            agenda:
                initialData.agenda || '',
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
            className="space-y-4"
        >

            <input
                type="number"
                name="association"
                value={formData.association}
                onChange={handleChange}
                placeholder="Association ID"
                className="w-full border p-3 rounded"
            />

            <input
                type="datetime-local"
                name="meeting_date"
                value={formData.meeting_date}
                onChange={handleChange}
                className="w-full border p-3 rounded"
            />

            <input
                type="text"
                name="location"
                value={formData.location}
                onChange={handleChange}
                placeholder="Location"
                className="w-full border p-3 rounded"
            />

            <textarea
                name="agenda"
                value={formData.agenda}
                onChange={handleChange}
                placeholder="Agenda"
                rows={5}
                className="w-full border p-3 rounded"
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

export default AssociationMeetingForm;