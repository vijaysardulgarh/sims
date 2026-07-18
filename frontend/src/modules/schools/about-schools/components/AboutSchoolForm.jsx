import { useState } from "react";

const AboutSchoolForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] = useState({

        school:
            initialData.school || "",

        history:
            initialData.history || "",

        vision:
            initialData.vision || "",

        mission:
            initialData.mission || "",
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
            className="space-y-6"
        >

            <div>

                <label className="block mb-2 text-sm font-medium text-gray-700">

                    School ID

                </label>

                <input
                    type="number"
                    name="school"
                    value={formData.school}
                    onChange={handleChange}
                    required
                    className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
                />

            </div>

            <div>

                <label className="block mb-2 text-sm font-medium text-gray-700">

                    History

                </label>

                <textarea
                    name="history"
                    rows={6}
                    value={formData.history}
                    onChange={handleChange}
                    className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
                />

            </div>

            <div>

                <label className="block mb-2 text-sm font-medium text-gray-700">

                    Vision

                </label>

                <textarea
                    name="vision"
                    rows={5}
                    value={formData.vision}
                    onChange={handleChange}
                    className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
                />

            </div>

            <div>

                <label className="block mb-2 text-sm font-medium text-gray-700">

                    Mission

                </label>

                <textarea
                    name="mission"
                    rows={5}
                    value={formData.mission}
                    onChange={handleChange}
                    className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
                />

            </div>

            <div className="flex justify-end">

                <button
                    type="submit"
                    className="rounded-lg bg-blue-600 px-6 py-2 font-medium text-white hover:bg-blue-700"
                >

                    Save

                </button>

            </div>

        </form>
    );
};

export default AboutSchoolForm;