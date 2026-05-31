import { useState } from "react";

const AboutSchoolForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] =
        useState({

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

        <form onSubmit={handleSubmit}>

            <div>

                <label>
                    School ID
                </label>

                <input
                    type="number"
                    name="school"
                    value={formData.school}
                    onChange={handleChange}
                />

            </div>

            <div>

                <label>
                    History
                </label>

                <textarea
                    name="history"
                    value={formData.history}
                    onChange={handleChange}
                />

            </div>

            <div>

                <label>
                    Vision
                </label>

                <textarea
                    name="vision"
                    value={formData.vision}
                    onChange={handleChange}
                />

            </div>

            <div>

                <label>
                    Mission
                </label>

                <textarea
                    name="mission"
                    value={formData.mission}
                    onChange={handleChange}
                />

            </div>

            <button type="submit">
                Save
            </button>

        </form>
    );
};

export default AboutSchoolForm;