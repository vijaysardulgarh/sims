const PeriodDefinitionForm = ({
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

                type === 'checkbox'

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

                <label>
                    Name
                </label>

                <input
                    type="text"
                    name="name"
                    value={
                        formData.name || ''
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

            <div>

                <label>
                    Code
                </label>

                <input
                    type="text"
                    name="code"
                    value={
                        formData.code || ''
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

            <div>

                <label>
                    Start Time
                </label>

                <input
                    type="time"
                    name="start_time"
                    value={
                        formData.start_time || ''
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

            <div>

                <label>
                    End Time
                </label>

                <input
                    type="time"
                    name="end_time"
                    value={
                        formData.end_time || ''
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

            <div>

                <label>
                    Period Type
                </label>

                <select

                    name="period_type"

                    value={
                        formData.period_type || ''
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
                >

                    <option value="">
                        Select
                    </option>

                    <option value="PERIOD">
                        Period
                    </option>

                    <option value="BREAK">
                        Break
                    </option>

                    <option value="LUNCH">
                        Lunch
                    </option>

                    <option value="ASSEMBLY">
                        Assembly
                    </option>

                </select>

            </div>

            <div>

                <label>
                    Display Order
                </label>

                <input
                    type="number"
                    name="display_order"
                    value={
                        formData.display_order || ''
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
                        name="is_active"
                        checked={
                            formData.is_active ?? true
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Active

                </label>

            </div>

        </div>

    );

};

export default PeriodDefinitionForm;