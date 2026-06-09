const BuildingForm = ({
    formData,
    setFormData,
}) => {

    return (

        <div className="space-y-6">

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                {/* NAME */}

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
                        Name
                    </label>

                    <input
                        type="text"
                        value={
                            formData.name || ""
                        }
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                name: e.target.value,
                            })
                        }
                        className="
                            w-full
                            px-4
                            py-3
                            border
                            border-gray-300
                            rounded-xl
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                        "
                    />

                </div>

                {/* CODE */}

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
                        Code
                    </label>

                    <input
                        type="text"
                        value={
                            formData.code || ""
                        }
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                code: e.target.value,
                            })
                        }
                        className="
                            w-full
                            px-4
                            py-3
                            border
                            border-gray-300
                            rounded-xl
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                        "
                    />

                </div>

                {/* FLOORS */}

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
                        Number of Floors
                    </label>

                    <input
                        type="number"
                        value={
                            formData.number_of_floors || ""
                        }
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                number_of_floors:
                                    e.target.value,
                            })
                        }
                        className="
                            w-full
                            px-4
                            py-3
                            border
                            border-gray-300
                            rounded-xl
                            focus:outline-none
                            focus:ring-2
                            focus:ring-blue-500
                        "
                    />

                </div>

                {/* ACTIVE */}

                <div
                    className="
                        flex
                        items-end
                    "
                >

                    <label
                        className="
                            flex
                            items-center
                            gap-3
                            cursor-pointer
                            h-12
                        "
                    >

                        <input
                            type="checkbox"
                            checked={
                                formData.is_active ?? true
                            }
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    is_active:
                                        e.target.checked,
                                })
                            }
                            className="
                                h-5
                                w-5
                            "
                        />

                        <span
                            className="
                                text-sm
                                font-medium
                                text-gray-700
                            "
                        >
                            Active
                        </span>

                    </label>

                </div>

            </div>

            {/* DESCRIPTION */}

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
                        setFormData({
                            ...formData,
                            description:
                                e.target.value,
                        })
                    }
                    className="
                        w-full
                        px-4
                        py-3
                        border
                        border-gray-300
                        rounded-xl
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                />

            </div>

        </div>

    );

};

export default BuildingForm;