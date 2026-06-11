const TimetableEntryForm = ({
    formData,
    setFormData,
}) => {

    const handleChange = (
        event
    ) => {

        const {
            name,
            value,
        } = event.target;

        setFormData({

            ...formData,

            [name]: value,

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
                    Day
                </label>

                <select

                    name="day"

                    value={
                        formData.day || ''
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

                </select>

            </div>

            <div>

                <label>
                    Period
                </label>

                <input
                    type="number"
                    name="period"
                    value={
                        formData.period || ''
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
                    Class
                </label>

                <input
                    type="number"
                    name="school_class"
                    value={
                        formData.school_class || ''
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
                    Section
                </label>

                <input
                    type="number"
                    name="section"
                    value={
                        formData.section || ''
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
                    Subject
                </label>

                <input
                    type="number"
                    name="subject"
                    value={
                        formData.subject || ''
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
                    Teacher
                </label>

                <input
                    type="number"
                    name="teacher"
                    value={
                        formData.teacher || ''
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
                    Room
                </label>

                <input
                    type="number"
                    name="room"
                    value={
                        formData.room || ''
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

        </div>

    );

};

export default TimetableEntryForm;