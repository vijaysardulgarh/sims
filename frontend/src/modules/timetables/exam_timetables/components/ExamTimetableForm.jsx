const ExamTimetableForm = ({
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
                    Exam
                </label>

                <input

                    type="number"

                    name="exam"

                    value={
                        formData.exam || ''
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
                    Effective From
                </label>

                <input

                    type="date"

                    name="effective_from"

                    value={
                        formData.effective_from || ''
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

export default ExamTimetableForm;