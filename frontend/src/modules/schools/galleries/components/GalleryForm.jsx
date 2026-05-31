import { useState } from "react";

const GalleryForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [formData, setFormData] =
        useState({

            school:
                initialData.school || "",

            title:
                initialData.title || "",

            description:
                initialData.description || "",

            display_order:
                initialData.display_order || 0,

            is_active:
                initialData.is_active ?? true,

            image: null,
        });

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked
        } = e.target;

        setFormData({

            ...formData,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        });
    };

    const handleImageChange = (e) => {

        setFormData({

            ...formData,

            image:
                e.target.files[0],
        });
    };

    const handleSubmit = (e) => {

        e.preventDefault();

        const payload =
            new FormData();

        Object.keys(formData)
            .forEach((key) => {

                if (
                    formData[key] !== null
                ) {

                    payload.append(
                        key,
                        formData[key]
                    );
                }
            });

        onSubmit(payload);
    };

    return (

        <form onSubmit={handleSubmit}>

            <input
                type="number"
                name="school"
                placeholder="School ID"
                value={formData.school}
                onChange={handleChange}
            />

            <input
                type="text"
                name="title"
                placeholder="Title"
                value={formData.title}
                onChange={handleChange}
            />

            <textarea
                name="description"
                placeholder="Description"
                value={
                    formData.description
                }
                onChange={handleChange}
            />

            <input
                type="file"
                onChange={
                    handleImageChange
                }
            />

            <input
                type="number"
                name="display_order"
                value={
                    formData.display_order
                }
                onChange={handleChange}
            />

            <label>

                Active

                <input
                    type="checkbox"
                    name="is_active"
                    checked={
                        formData.is_active
                    }
                    onChange={
                        handleChange
                    }
                />

            </label>

            <button type="submit">

                Save

            </button>

        </form>
    );
};

export default GalleryForm;