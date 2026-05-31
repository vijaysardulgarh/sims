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

        message:
            initialData.message || "",

        joining_date:
            initialData.joining_date || "",
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
                <label>School</label>

                <input
                    type="number"
                    name="school"
                    value={formData.school}
                    onChange={handleChange}
                />
            </div>

            <div>
                <label>Name</label>

                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                />
            </div>

            <div>
                <label>Qualification</label>

                <input
                    type="text"
                    name="qualification"
                    value={formData.qualification}
                    onChange={handleChange}
                />
            </div>

            <div>
                <label>Joining Date</label>

                <input
                    type="date"
                    name="joining_date"
                    value={formData.joining_date}
                    onChange={handleChange}
                />
            </div>

            <div>
                <label>Message</label>

                <textarea
                    name="message"
                    rows="6"
                    value={formData.message}
                    onChange={handleChange}
                />
            </div>

            <button type="submit">
                Save
            </button>

        </form>
    );
};

export default PrincipalForm;