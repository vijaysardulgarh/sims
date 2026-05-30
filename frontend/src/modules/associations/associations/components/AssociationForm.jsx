// ============================================
// IMPORTS
// ============================================

import {
    useState,
    useEffect
} from 'react';

// ============================================
// COMPONENT
// ============================================

const AssociationForm = ({
    initialData = {},
    onSubmit,
    loading,
}) => {

    const [formData, setFormData] =
        useState({

            name: '',

            association_type: 'Club',

            status: 'Active',

            description: '',

            tasks: '',

            priority: 0,

            show_on_website: true,
        });

    // ========================================
    // LOAD INITIAL DATA
    // ========================================

    useEffect(() => {

        if (
            initialData &&
            Object.keys(initialData).length > 0
        ) {

            setFormData({

                name:
                    initialData.name || '',

                association_type:
                    initialData.association_type || 'Club',

                status:
                    initialData.status || 'Active',

                description:
                    initialData.description || '',

                tasks:
                    initialData.tasks || '',

                priority:
                    initialData.priority || 0,

                show_on_website:
                    initialData.show_on_website ?? true,
            });

        }

    }, [initialData]);

    // ========================================
    // HANDLE CHANGE
    // ========================================

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
                type === 'checkbox'
                    ? checked
                    : value,

        }));

    };

    // ========================================
    // HANDLE SUBMIT
    // ========================================

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);

    };

    // ========================================
    // UI
    // ========================================

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-6"
        >

            <div>

                <label className="block mb-2 font-medium">
                    Name
                </label>

                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="w-full border rounded-xl p-3"
                    required
                />

            </div>

            <div>

                <label className="block mb-2 font-medium">
                    Association Type
                </label>

                <select
                    name="association_type"
                    value={formData.association_type}
                    onChange={handleChange}
                    className="w-full border rounded-xl p-3"
                >

                    <option value="Club">
                        Club
                    </option>

                    <option value="Committee">
                        Committee
                    </option>

                    <option value="Nodal">
                        Nodal
                    </option>

                </select>

            </div>

            <div>

                <label className="block mb-2 font-medium">
                    Status
                </label>

                <select
                    name="status"
                    value={formData.status}
                    onChange={handleChange}
                    className="w-full border rounded-xl p-3"
                >

                    <option value="Active">
                        Active
                    </option>

                    <option value="Inactive">
                        Inactive
                    </option>

                    <option value="Archived">
                        Archived
                    </option>

                </select>

            </div>

            <div>

                <label className="block mb-2 font-medium">
                    Description
                </label>

                <textarea
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    rows={4}
                    className="w-full border rounded-xl p-3"
                />

            </div>

            <div>

                <label className="block mb-2 font-medium">
                    Tasks
                </label>

                <textarea
                    name="tasks"
                    value={formData.tasks}
                    onChange={handleChange}
                    rows={4}
                    className="w-full border rounded-xl p-3"
                />

            </div>

            <div>

                <label className="block mb-2 font-medium">
                    Priority
                </label>

                <input
                    type="number"
                    name="priority"
                    value={formData.priority}
                    onChange={handleChange}
                    className="w-full border rounded-xl p-3"
                />

            </div>

            <div className="flex items-center gap-3">

                <input
                    type="checkbox"
                    name="show_on_website"
                    checked={formData.show_on_website}
                    onChange={handleChange}
                />

                <label>
                    Show on Website
                </label>

            </div>

            <button
                type="submit"
                disabled={loading}
                className="
                    bg-black
                    text-white
                    px-6
                    py-3
                    rounded-xl
                "
            >

                {
                    loading
                        ? 'Saving...'
                        : 'Save Association'
                }

            </button>

        </form>

    );

};

export default AssociationForm;