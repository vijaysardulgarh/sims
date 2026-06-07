import React from "react";

const AcademicSessionForm = ({
    formData,
    setFormData,
    loading = false,
}) => {

    const handleChange = (
        field,
        value
    ) => {

        setFormData((prev) => ({

            ...prev,

            [field]: value,

        }));
    };

    return (

        <div
            className="
                bg-white
                rounded-2xl
                border
                border-gray-200
                shadow-sm
                p-6
            "
        >

            {/* Header */}

            <div className="mb-6">

                <h2
                    className="
                        text-lg
                        font-semibold
                        text-gray-900
                    "
                >
                    Academic Session Information
                </h2>

                <p
                    className="
                        mt-1
                        text-sm
                        text-gray-500
                    "
                >
                    Configure the academic session details
                    for the school.
                </p>

            </div>

            {/* Form Fields */}

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* Session Name */}

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
                        Session Name
                        <span className="text-red-500 ml-1">
                            *
                        </span>
                    </label>

                    <input

                        type="text"

                        value={formData.name || ""}

                        onChange={(e) =>
                            handleChange(
                                "name",
                                e.target.value
                            )
                        }

                        placeholder="2025-2026"

                        disabled={loading}

                        required

                        className="
                            w-full
                            rounded-lg
                            border
                            border-gray-300
                            px-4
                            py-3
                            text-sm
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                            focus:border-blue-500
                            disabled:bg-gray-100
                        "

                    />

                    <p
                        className="
                            mt-2
                            text-xs
                            text-gray-500
                        "
                    >
                        Example: 2025-2026
                    </p>

                </div>

                {/* Current Session */}

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
                        Session Status
                    </label>

                    <div
                        className="
                            flex
                            items-center
                            rounded-lg
                            border
                            border-gray-200
                            px-4
                            py-3
                            bg-gray-50
                        "
                    >

                        <input

                            id="is_current"

                            type="checkbox"

                            checked={
                                formData.is_current || false
                            }

                            onChange={(e) =>
                                handleChange(
                                    "is_current",
                                    e.target.checked
                                )
                            }

                            disabled={loading}

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

                            htmlFor="is_current"

                            className="
                                ml-3
                                text-sm
                                text-gray-700
                                cursor-pointer
                            "

                        >
                            Set as Current Academic Session
                        </label>

                    </div>

                    <p
                        className="
                            mt-2
                            text-xs
                            text-gray-500
                        "
                    >
                        Only one session should normally be
                        marked as current.
                    </p>

                </div>

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
                        <span className="text-red-500 ml-1">
                            *
                        </span>
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

                        disabled={loading}

                        required

                        className="
                            w-full
                            rounded-lg
                            border
                            border-gray-300
                            px-4
                            py-3
                            text-sm
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                            focus:border-blue-500
                            disabled:bg-gray-100
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
                        <span className="text-red-500 ml-1">
                            *
                        </span>
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

                        min={
                            formData.start_date || ""
                        }

                        disabled={loading}

                        required

                        className="
                            w-full
                            rounded-lg
                            border
                            border-gray-300
                            px-4
                            py-3
                            text-sm
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                            focus:border-blue-500
                            disabled:bg-gray-100
                        "

                    />

                </div>

            </div>

        </div>

    );
};

export default AcademicSessionForm;