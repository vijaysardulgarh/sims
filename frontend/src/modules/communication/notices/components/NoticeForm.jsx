const NoticeForm = ({
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
                        Notice Title
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
                        placeholder="Enter notice title"
                    />

                </div>

                {/* Notice Type */}

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
                        Notice Type
                    </label>

                    <select
                        value={
                            formData.notice_type || "GENERAL"
                        }
                        onChange={(e) =>
                            handleChange(
                                "notice_type",
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

                        <option value="GENERAL">
                            General
                        </option>

                        <option value="HOLIDAY">
                            Holiday
                        </option>

                        <option value="EXAM">
                            Exam
                        </option>

                        <option value="FEE">
                            Fee
                        </option>

                        <option value="ADMISSION">
                            Admission
                        </option>

                        <option value="STAFF">
                            Staff
                        </option>

                        <option value="TRANSPORT">
                            Transport
                        </option>

                        <option value="URGENT">
                            Urgent
                        </option>

                    </select>

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
                    placeholder="Enter notice description"
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

                {/* Expiry Date */}

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
                        Expiry Date
                    </label>

                    <input
                        type="date"
                        value={
                            formData.expiry_date || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "expiry_date",
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

            {/* Published */}

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
                        formData.is_published ?? true
                    }
                    onChange={(e) =>
                        handleChange(
                            "is_published",
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
                    Published
                </label>

            </div>

        </div>

    );

};

export default NoticeForm;