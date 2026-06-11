const TimetableVersionForm = ({
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
                    Timetable
                </label>

                <input
                    type="number"
                    name="timetable"
                    value={
                        formData.timetable || ''
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
                    Version Number
                </label>

                <input
                    type="text"
                    name="version_number"
                    value={
                        formData.version_number || ''
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

                <label>
                    Version Name
                </label>

                <input
                    type="text"
                    name="version_name"
                    value={
                        formData.version_name || ''
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

                <label>
                    Change Summary
                </label>

                <textarea

                    name="change_summary"

                    rows="5"

                    value={
                        formData.change_summary || ''
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

                    Active Version

                </label>

            </div>

        </div>

    );

};

export default TimetableVersionForm;