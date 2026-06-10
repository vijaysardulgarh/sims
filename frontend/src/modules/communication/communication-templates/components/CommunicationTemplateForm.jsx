import {
    useEffect,
    useState,
} from "react";

import api from "../../../../services/api/axios";

const CommunicationTemplateForm = ({
    formData,
    setFormData,
}) => {

    const [
        categories,
        setCategories,
    ] = useState([]);

    useEffect(() => {

        loadCategories();

    }, []);

    const loadCategories = async () => {

        try {

            const response =
                await api.get(
                    "/communications/communication-categories/"
                );

            setCategories(
                response.data.results ||
                response.data
            );

        }

        catch (error) {

            console.error(error);

        }

    };

    const handleChange = (
        field,
        value
    ) => {

        setFormData({
            ...formData,
            [field]: value,
        });

    };

    return (

        <div className="space-y-6">

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* Category */}

                <div>

                    <label
                        className="
                            block
                            text-sm
                            font-medium
                            text-gray-700
                            mb-2
                        "
                    >
                        Category
                    </label>

                    <select
                        value={
                            formData.category || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "category",
                                e.target.value
                            )
                        }
                        className="
                            w-full
                            px-4
                            py-3
                            border
                            border-gray-300
                            rounded-xl
                            shadow-sm
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                        "
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

                {/* Template Name */}

                <div>

                    <label
                        className="
                            block
                            text-sm
                            font-medium
                            text-gray-700
                            mb-2
                        "
                    >
                        Template Name
                    </label>

                    <input
                        type="text"
                        value={
                            formData.name || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "name",
                                e.target.value
                            )
                        }
                        className="
                            w-full
                            px-4
                            py-3
                            border
                            border-gray-300
                            rounded-xl
                            shadow-sm
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                        "
                        placeholder="Enter template name"
                    />

                </div>

            </div>

            {/* Subject */}

            <div>

                <label
                    className="
                        block
                        text-sm
                        font-medium
                        text-gray-700
                        mb-2
                    "
                >
                    Subject
                </label>

                <input
                    type="text"
                    value={
                        formData.subject || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "subject",
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        px-4
                        py-3
                        border
                        border-gray-300
                        rounded-xl
                        shadow-sm
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                    placeholder="Enter subject"
                />

            </div>

            {/* Template Body */}

            <div>

                <label
                    className="
                        block
                        text-sm
                        font-medium
                        text-gray-700
                        mb-2
                    "
                >
                    Template Content
                </label>

                <textarea
                    rows={10}
                    value={
                        formData.content || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "content",
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        px-4
                        py-3
                        border
                        border-gray-300
                        rounded-xl
                        shadow-sm
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                    placeholder="Enter template content"
                />

            </div>

            {/* Active */}

            <div
                className="
                    flex
                    items-center
                    gap-3
                "
            >

                <input
                    type="checkbox"
                    checked={
                        formData.is_active ?? true
                    }
                    onChange={(e) =>
                        handleChange(
                            "is_active",
                            e.target.checked
                        )
                    }
                    className="
                        h-4
                        w-4
                        rounded
                        border-gray-300
                        text-blue-600
                        focus:ring-blue-500
                    "
                />

                <label
                    className="
                        text-sm
                        font-medium
                        text-gray-700
                    "
                >
                    Active
                </label>

            </div>

        </div>

    );

};

export default CommunicationTemplateForm;