const TeacherAvailabilityForm = ({
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

                    <option value="MON">
                        Monday
                    </option>

                    <option value="TUE">
                        Tuesday
                    </option>

                    <option value="WED">
                        Wednesday
                    </option>

                    <option value="THU">
                        Thursday
                    </option>

                    <option value="FRI">
                        Friday
                    </option>

                    <option value="SAT">
                        Saturday
                    </option>

                </select>

            </div>

            <div>

                <label>
                    Available From
                </label>

                <input
                    type="time"
                    name="available_from"
                    value={
                        formData.available_from || ''
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
                    Available To
                </label>

                <input
                    type="time"
                    name="available_to"
                    value={
                        formData.available_to || ''
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
                    Availability Type
                </label>

                <select

                    name="availability_type"

                    value={
                        formData.availability_type || ''
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

                    <option value="AVAILABLE">
                        Available
                    </option>

                    <option value="UNAVAILABLE">
                        Unavailable
                    </option>

                    <option value="PREFERRED">
                        Preferred
                    </option>

                </select>

            </div>

        </div>

    );

};

export default TeacherAvailabilityForm;