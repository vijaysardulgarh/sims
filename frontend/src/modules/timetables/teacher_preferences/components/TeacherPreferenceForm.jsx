const TeacherPreferenceForm = ({
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
                    Preferred Period
                </label>

                <input
                    type="number"
                    name="preferred_period"
                    value={
                        formData.preferred_period || ''
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
                    Preference Level
                </label>

                <select

                    name="preference_level"

                    value={
                        formData.preference_level || ''
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

                    <option value="HIGH">
                        High
                    </option>

                    <option value="MEDIUM">
                        Medium
                    </option>

                    <option value="LOW">
                        Low
                    </option>

                </select>

            </div>

            <div
                className="
                    md:col-span-2
                "
            >

                <label>
                    Remarks
                </label>

                <textarea

                    name="remarks"

                    rows="4"

                    value={
                        formData.remarks || ''
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

export default TeacherPreferenceForm;