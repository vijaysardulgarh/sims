const FAQForm = ({
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

            {/* Question */}

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
                    Question
                </label>

                <input
                    type="text"
                    value={
                        formData.question || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "question",
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
                    placeholder="Enter FAQ question"
                />

            </div>

            {/* Answer */}

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
                    Answer
                </label>

                <textarea
                    rows={6}
                    value={
                        formData.answer || ""
                    }
                    onChange={(e) =>
                        handleChange(
                            "answer",
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
                    placeholder="Enter answer"
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
                            formData.category || "general"
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

                        <option value="admission">
                            Admission
                        </option>

                        <option value="fees">
                            Fees
                        </option>

                        <option value="academics">
                            Academics
                        </option>

                        <option value="facilities">
                            Facilities
                        </option>

                        <option value="general">
                            General
                        </option>

                    </select>

                </div>

                {/* Order */}

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
                        Display Order
                    </label>

                    <input
                        type="number"
                        value={
                            formData.order ?? 0
                        }
                        onChange={(e) =>
                            handleChange(
                                "order",
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
                        min="0"
                    />

                </div>

            </div>

        </div>

    );

};

export default FAQForm;