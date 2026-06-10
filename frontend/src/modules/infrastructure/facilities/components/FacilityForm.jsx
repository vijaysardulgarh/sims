const FacilityForm = ({
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

            {/* FACILITY NAME */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Facility Name
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <input
                    type="text"
                    required
                    placeholder="Campus WiFi"
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

            {/* FACILITY TYPE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Facility Type
                    <span className="ml-1 text-red-500">
                        *
                    </span>

                </label>

                <select
                    required
                    value={
                        formData.facility_type ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'facility_type',
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
                        Select Facility Type
                    </option>

                    <option value="CCTV">
                        CCTV
                    </option>

                    <option value="WIFI">
                        WiFi
                    </option>

                    <option value="RO_WATER">
                        RO Water
                    </option>

                    <option value="MEDICAL_ROOM">
                        Medical Room
                    </option>

                    <option value="TRANSPORT">
                        Transport
                    </option>

                    <option value="HOSTEL">
                        Hostel
                    </option>

                    <option value="POWER_BACKUP">
                        Power Backup
                    </option>

                    <option value="BIOMETRIC">
                        Biometric System
                    </option>

                    <option value="PA_SYSTEM">
                        Public Address System
                    </option>

                    <option value="OTHER">
                        Other
                    </option>

                </select>

            </div>

            {/* INSTALLATION DATE */}

            <div className="md:col-span-6">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Installation Date

                </label>

                <input
                    type="date"
                    value={
                        formData.installation_date ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'installation_date',
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

            {/* AVAILABLE */}

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
                            formData.available ??
                            true
                        }
                        onChange={(e) =>
                            handleChange(
                                'available',
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

                            Available

                        </p>

                        <p className="text-sm text-gray-500">

                            Facility is currently
                            available for use.

                        </p>

                    </div>

                </label>

            </div>

            {/* DESCRIPTION */}

            <div className="md:col-span-12">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Description

                </label>

                <textarea
                    rows={4}
                    placeholder="Enter facility description..."
                    value={
                        formData.description ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'description',
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

            {/* REMARKS */}

            <div className="md:col-span-12">

                <label className="mb-2 block text-sm font-medium text-gray-700">

                    Remarks

                </label>

                <textarea
                    rows={3}
                    placeholder="Additional remarks..."
                    value={
                        formData.remarks ||
                        ''
                    }
                    onChange={(e) =>
                        handleChange(
                            'remarks',
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

        </div>
    );
};

export default FacilityForm;