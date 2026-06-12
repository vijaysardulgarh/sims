const BellScheduleForm = ({
    formData,
    setFormData,
}) => {

    const handleChange = (
        event
    ) => {

        const {
            name,
            value,
            type,
            checked,
        } = event.target;

        setFormData({

            ...formData,

            [name]:

                type === "checkbox"

                    ? checked

                    : value,

        });

    };

    return (

        <div
            className="
                grid
                grid-cols-1
                md:grid-cols-2
                gap-6
            "
        >

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Name
                </label>

                <input

                    type="text"

                    name="name"

                    value={
                        formData.name || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "

                    required

                />

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Code
                </label>

                <input

                    type="text"

                    name="code"

                    value={
                        formData.code || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "

                    required

                />

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Display Order
                </label>

                <input

                    type="number"

                    name="display_order"

                    value={
                        formData.display_order || ""
                    }

                    onChange={
                        handleChange
                    }

                    min="1"

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "

                />

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Start Date
                </label>

                <input

                    type="date"

                    name="start_date"

                    value={
                        formData.start_date || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "

                    required

                />

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    End Date
                </label>

                <input

                    type="date"

                    name="end_date"

                    value={
                        formData.end_date || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "

                />

            </div>

            <div
                className="
                    md:col-span-2
                "
            >

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Description
                </label>

                <textarea

                    name="description"

                    rows={4}

                    value={
                        formData.description || ""
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "

                />

            </div>

            <div
                className="
                    md:col-span-2
                "
            >

                <label
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input

                        type="checkbox"

                        name="is_default"

                        checked={
                            formData.is_default || false
                        }

                        onChange={
                            handleChange
                        }

                    />

                    Default Bell Schedule

                </label>

            </div>

        </div>

    );

};

export default BellScheduleForm;