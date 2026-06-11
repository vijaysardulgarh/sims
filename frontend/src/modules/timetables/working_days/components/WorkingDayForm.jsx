const WorkingDayForm = ({
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
                    Day Name
                </label>

                <select

                    name="day_name"

                    value={
                        formData.day_name || ''
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
                        Select Day
                    </option>

                    <option value="MONDAY">
                        Monday
                    </option>

                    <option value="TUESDAY">
                        Tuesday
                    </option>

                    <option value="WEDNESDAY">
                        Wednesday
                    </option>

                    <option value="THURSDAY">
                        Thursday
                    </option>

                    <option value="FRIDAY">
                        Friday
                    </option>

                    <option value="SATURDAY">
                        Saturday
                    </option>

                    <option value="SUNDAY">
                        Sunday
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

                        name="is_working_day"

                        checked={
                            formData.is_working_day ?? true
                        }

                        onChange={
                            handleChange
                        }

                    />

                    Working Day

                </label>

            </div>

        </div>

    );

};

export default WorkingDayForm;