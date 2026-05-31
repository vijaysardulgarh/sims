import {
    useEffect,
    useState,
} from 'react';

import api from '../../../../services/api/axios';

const CommunicationTemplateForm = ({
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
                    Template Name
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.name || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            name:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Subject
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.subject || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            subject:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label>
                    Template Body
                </label>

                <textarea
                    rows="8"
                    className="form-control"
                    value={
                        formData.content || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            content:
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

export default CommunicationTemplateForm;