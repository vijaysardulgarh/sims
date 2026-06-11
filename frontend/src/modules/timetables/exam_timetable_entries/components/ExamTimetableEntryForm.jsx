const ExamTimetableEntryForm = ({
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
                    Exam Timetable
                </label>

                <input
                    type="number"
                    name="exam_timetable"
                    value={
                        formData.exam_timetable || ''
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
                    Exam Date
                </label>

                <input
                    type="date"
                    name="exam_date"
                    value={
                        formData.exam_date || ''
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
                    Invigilator
                </label>

                <input
                    type="number"
                    name="invigilator"
                    value={
                        formData.invigilator || ''
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

export default ExamTimetableEntryForm;