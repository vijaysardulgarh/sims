const TeacherWorkloadForm = ({
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
                    Maximum Periods Per Day
                </label>

                <input
                    type="number"
                    name="maximum_periods_per_day"
                    value={
                        formData.maximum_periods_per_day || ''
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
                    Maximum Periods Per Week
                </label>

                <input
                    type="number"
                    name="maximum_periods_per_week"
                    value={
                        formData.maximum_periods_per_week || ''
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
                    Minimum Periods Per Week
                </label>

                <input
                    type="number"
                    name="minimum_periods_per_week"
                    value={
                        formData.minimum_periods_per_week || ''
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

export default TeacherWorkloadForm;