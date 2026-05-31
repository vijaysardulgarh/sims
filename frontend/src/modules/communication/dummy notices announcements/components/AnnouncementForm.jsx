import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const AnnouncementForm = ({
    formData,
    setFormData,
}) => {

    const [
        categories,
        setCategories
    ] = useState([]);

    useEffect(() => {

        loadCategories();

    }, []);

    const loadCategories = async () => {

        try {

            const response =
                await api.get(
                    '/communications/communication-categories/'
                );

            setCategories(
                response.data.results ||
                response.data
            );

        } catch (error) {

            console.error(error);
        }
    };

    return (
        <>
            <div className="mb-3">

                <label>
                    Category
                </label>

                <select
                    className="form-control"
                    value={
                        formData.category || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            category:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Category
                    </option>

                    {categories.map(
                        (category) => (

                            <option
                                key={category.id}
                                value={category.id}
                            >
                                {category.name}
                            </option>

                        )
                    )}

                </select>

            </div>

            <div className="mb-3">

                <label>
                    Title
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.title || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            title:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Announcement
                </label>

                <textarea
                    rows="8"
                    className="form-control"
                    value={
                        formData.message || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            message:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Publish Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.publish_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            publish_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Expiry Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.expiry_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            expiry_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="form-check">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.is_active ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            is_active:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Active
                </label>

            </div>

        </>
    );
};

export default AnnouncementForm;