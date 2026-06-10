const CircularForm = ({
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

                {/* Reference Number */}

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
                        Reference Number
                    </label>

                    <input
                        type="text"
                        value={
                            formData.reference_number || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "reference_number",
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
                    />

                </div>

                {/* Circular Type */}

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
                        Circular Type
                    </label>

                    <select
                        value={
                            formData.circular_type || "OTHER"
                        }
                        onChange={(e) =>
                            handleChange(
                                "circular_type",
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

                        <option value="GOVERNMENT">
                            Government
                        </option>

                        <option value="CBSE">
                            CBSE
                        </option>

                        <option value="ADMINISTRATIVE">
                            Administrative
                        </option>

                        <option value="POLICY">
                            Policy
                        </option>

                        <option value="DEPARTMENT">
                            Department
                        </option>

                        <option value="OTHER">
                            Other
                        </option>

                    </select>

                </div>

            </div>

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
                    Title
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
                />

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
                    rows={6}
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
                    "
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

                {/* Issue Date */}

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
                        Issue Date
                    </label>

                    <input
                        type="date"
                        value={
                            formData.issue_date || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "issue_date",
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

                {/* Effective Date */}

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
                        Effective Date
                    </label>

                    <input
                        type="date"
                        value={
                            formData.effective_date || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "effective_date",
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

export default CircularForm;