const EventForm = ({
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
                    Event Title
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
                    placeholder="Enter event title"
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
                    "
                    placeholder="Enter event description"
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

                {/* Start Date */}

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
                        Start Date
                    </label>

                    <input
                        type="date"
                        value={
                            formData.start_date || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "start_date",
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

                {/* End Date */}

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
                        End Date
                    </label>

                    <input
                        type="date"
                        value={
                            formData.end_date || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "end_date",
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

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* Start Time */}

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
                        Start Time
                    </label>

                    <input
                        type="time"
                        value={
                            formData.start_time || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "start_time",
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

                {/* End Time */}

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
                        End Time
                    </label>

                    <input
                        type="time"
                        value={
                            formData.end_time || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "end_time",
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

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* Venue */}

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
                        Venue
                    </label>

                    <input
                        type="text"
                        value={
                            formData.venue || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "venue",
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
                        "
                    />

                </div>

                {/* Organizer */}

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
                        Organizer
                    </label>

                    <input
                        type="text"
                        value={
                            formData.organizer || ""
                        }
                        onChange={(e) =>
                            handleChange(
                                "organizer",
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
                        "
                    />

                </div>

            </div>

            <div className="flex gap-6">

                <label className="flex items-center gap-2">

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

                    Featured Event

                </label>

                <label className="flex items-center gap-2">

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

export default EventForm;