import { useState } from "react";

const PrincipalForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] = useState({

        school: initialData.school || "",

        name: initialData.name || "",

        qualification:
            initialData.qualification || "",

        joining_date:
            initialData.joining_date || "",

        message:
            initialData.message || "",

        display_order:
            initialData.display_order || 0,

        photo: null,

    });

    const handleChange = (e) => {

        const {
            name,
            value,
            files,
            type,
        } = e.target;

        setFormData({

            ...formData,

            [name]:
                type === "file"
                    ? files[0]
                    : value,

        });

    };

    const handleSubmit = (e) => {

        e.preventDefault();

        const data = new FormData();

        Object.keys(formData).forEach((key) => {

            if (
                formData[key] !== null &&
                formData[key] !== ""
            ) {
                data.append(
                    key,
                    formData[key]
                );
            }

        });

        onSubmit(data);

    };

    return (

        <form
            onSubmit={handleSubmit}
            className="bg-white rounded-xl shadow p-6 space-y-6"
        >

            <h2 className="text-2xl font-bold">
                Principal Information
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                {/* School */}

                <div>

                    <label className="block mb-2 text-sm font-medium">

                        School ID

                    </label>

                    <input
                        type="number"
                        name="school"
                        value={formData.school}
                        onChange={handleChange}
                        className="w-full border rounded-lg px-4 py-2"
                    />

                </div>

                {/* Name */}

                <div>

                    <label className="block mb-2 text-sm font-medium">

                        Name

                    </label>

                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        className="w-full border rounded-lg px-4 py-2"
                        required
                    />

                </div>

                {/* Qualification */}

                <div>

                    <label className="block mb-2 text-sm font-medium">

                        Qualification

                    </label>

                    <input
                        type="text"
                        name="qualification"
                        value={formData.qualification}
                        onChange={handleChange}
                        className="w-full border rounded-lg px-4 py-2"
                    />

                </div>

                {/* Joining Date */}

                <div>

                    <label className="block mb-2 text-sm font-medium">

                        Joining Date

                    </label>

                    <input
                        type="date"
                        name="joining_date"
                        value={formData.joining_date}
                        onChange={handleChange}
                        className="w-full border rounded-lg px-4 py-2"
                    />

                </div>

                {/* Display Order */}

                <div>

                    <label className="block mb-2 text-sm font-medium">

                        Display Order

                    </label>

                    <input
                        type="number"
                        name="display_order"
                        value={formData.display_order}
                        onChange={handleChange}
                        className="w-full border rounded-lg px-4 py-2"
                    />

                </div>

                {/* Photo */}

                <div>

                    <label className="block mb-2 text-sm font-medium">

                        Photo

                    </label>

                    <input
                        type="file"
                        name="photo"
                        accept="image/*"
                        onChange={handleChange}
                        className="w-full border rounded-lg px-4 py-2"
                    />

                </div>

            </div>

            {/* Message */}

            <div>

                <label className="block mb-2 text-sm font-medium">

                    Principal's Message

                </label>

                <textarea
                    name="message"
                    rows="8"
                    value={formData.message}
                    onChange={handleChange}
                    className="w-full border rounded-lg px-4 py-2"
                />

            </div>

            <div className="flex justify-end">

                <button
                    type="submit"
                    className="
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        px-6
                        py-2
                        rounded-lg
                    "
                >
                    Save Principal
                </button>

            </div>

        </form>

    );

};

export default PrincipalForm;