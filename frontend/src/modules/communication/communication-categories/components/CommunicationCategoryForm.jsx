const CommunicationCategoryForm = ({
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

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* Name */}

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
                        Category Name
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
                            focus:border-blue-500
                        "
                        placeholder="Enter category name"
                    />

                </div>

                {/* Code */}

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
                        Category Code
                    </label>

                    <input
                        type="text"
                        value={
                            formData.code || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "code",
                                e.target.value.toUpperCase()
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
                            focus:border-blue-500
                        "
                        placeholder="e.g. ACADEMIC"
                    />

                </div>

            </div>

            {/* Description */}

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
                    Description
                </label>

                <textarea
                    rows={5}
                    value={
                        formData.description || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "description",
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
                        focus:border-blue-500
                    "
                    placeholder="Enter description"
                />

            </div>

            {/* Active */}

            <div
                className="
                    flex
                    items-center
                    gap-3
                    pt-2
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

export default CommunicationCategoryForm;