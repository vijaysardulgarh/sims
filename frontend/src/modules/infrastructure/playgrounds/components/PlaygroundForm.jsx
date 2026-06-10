const PlaygroundForm = ({
    formData,
    setFormData,
}) => {

    const handleChange = (
        field,
        value
    ) => {

        setFormData(
            (prev) => ({
                ...prev,
                [field]: value,
            })
        );
    };

    return (

        <div className="grid grid-cols-1 gap-6 md:grid-cols-12">

            {/* PLAYGROUND NAME */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Playground Name
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="text"
                    required
                    placeholder="Main Cricket Ground"
                    value={
                        formData.name ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'name',
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                />

            </div>

            {/* PLAYGROUND TYPE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Playground Type
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <select
                    required
                    value={
                        formData.playground_type ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'playground_type',
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                >

                    <option value="">
                        Select Playground Type
                    </option>

                    <option value="CRICKET">
                        Cricket Ground
                    </option>

                    <option value="FOOTBALL">
                        Football Ground
                    </option>

                    <option value="BASKETBALL">
                        Basketball Court
                    </option>

                    <option value="VOLLEYBALL">
                        Volleyball Court
                    </option>

                    <option value="BADMINTON">
                        Badminton Court
                    </option>

                    <option value="ATHLETICS">
                        Athletics Track
                    </option>

                    <option value="MULTIPURPOSE">
                        Multi Purpose Ground
                    </option>

                    <option value="OTHER">
                        Other
                    </option>

                </select>

            </div>

            {/* AREA */}

            <div className="md:col-span-4">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Area (sq.ft)

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="5000"
                    value={
                        formData.area || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'area',
                            Number(
                                e.target.value
                            ) || ''
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                />

            </div>

            {/* CAPACITY */}

            <div className="md:col-span-4">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Capacity

                </label>

                <input
                    type="number"
                    min="0"
                    placeholder="1000"
                    value={
                        formData.capacity || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'capacity',
                            Number(
                                e.target.value
                            ) || ''
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                />

            </div>

            {/* LOCATION */}

            <div className="md:col-span-4">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Location

                </label>

                <input
                    type="text"
                    placeholder="North Campus"
                    value={
                        formData.location || ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'location',
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        rounded-lg
                        border
                        border-gray-300
                        px-3
                        py-2
                        text-sm
                        focus:border-blue-500
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-200
                    "
                />

            </div>

            {/* COVERED */}

            <div className="md:col-span-6">

                <label
                    className="
                        flex
                        cursor-pointer
                        items-center
                        gap-3
                        rounded-lg
                        border
                        border-gray-200
                        p-4
                    "
                >

                    <input
                        type="checkbox"
                        checked={
                            formData.covered ||
                            false
                        }
                        onChange={(e) =>
                            handleChange(
                                'covered',
                                e.target.checked
                            )
                        }
                        className="
                            h-4
                            w-4
                            rounded
                            border-gray-300
                        "
                    />

                    <div>

                        <p className="font-medium text-gray-700">

                            Covered Playground

                        </p>

                        <p className="text-sm text-gray-500">

                            Enable if the playground
                            is covered or indoor.

                        </p>

                    </div>

                </label>

            </div>

            {/* ACTIVE */}

            <div className="md:col-span-6">

                <label
                    className="
                        flex
                        cursor-pointer
                        items-center
                        gap-3
                        rounded-lg
                        border
                        border-gray-200
                        p-4
                    "
                >

                    <input
                        type="checkbox"
                        checked={
                            formData.is_active ??
                            true
                        }
                        onChange={(e) =>
                            handleChange(
                                'is_active',
                                e.target.checked
                            )
                        }
                        className="
                            h-4
                            w-4
                            rounded
                            border-gray-300
                        "
                    />

                    <div>

                        <p className="font-medium text-gray-700">

                            Active

                        </p>

                        <p className="text-sm text-gray-500">

                            Mark this playground as
                            available for use.

                        </p>

                    </div>

                </label>

            </div>

        </div>
    );
};

export default PlaygroundForm;