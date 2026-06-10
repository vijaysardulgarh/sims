const NewsForm = ({
    formData,
    setFormData,
}) => {

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

            {/* Title */}

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
                    News Title
                </label>

                <input
                    type="text"
                    value={
                        formData.title || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "title",
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
                    placeholder="Enter news title"
                />

            </div>

            {/* Slug */}

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
                    Slug
                </label>

                <input
                    type="text"
                    value={
                        formData.slug || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "slug",
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
                    placeholder="school-annual-function-2026"
                />

            </div>

            {/* Summary */}

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
                    Summary
                </label>

                <textarea
                    rows={3}
                    value={
                        formData.summary || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "summary",
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
                    placeholder="Short summary"
                />

            </div>

            {/* Content */}

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
                    Content
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
                    placeholder="Enter news content"
                />

            </div>

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* Publish Date */}

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
                        Publish Date
                    </label>

                    <input
                        type="date"
                        value={
                            formData.publish_date || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "publish_date",
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
                    />

                </div>

            </div>

            {/* Checkboxes */}

            <div
                className="
                    flex
                    flex-wrap
                    gap-6
                "
            >

                <label
                    className="
                        flex
                        items-center
                        gap-2
                    "
                >

                    <input
                        type="checkbox"
                        checked={
                            formData.is_featured ?? false
                        }
                        onChange={(e) =>
                            handleChange(
                                "is_featured",
                                e.target.checked
                            )
                        }
                    />

                    Featured News

                </label>

                <label
                    className="
                        flex
                        items-center
                        gap-2
                    "
                >

                    <input
                        type="checkbox"
                        checked={
                            formData.is_published ?? true
                        }
                        onChange={(e) =>
                            handleChange(
                                "is_published",
                                e.target.checked
                            )
                        }
                    />

                    Published

                </label>

            </div>

        </div>

    );

};

export default NewsForm;