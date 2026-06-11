const TimetablePublicationForm = ({
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
                    Publication Type
                </label>

                <select

                    name="publication_type"

                    value={
                        formData.publication_type || ''
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

                    <option value="STUDENT">
                        Student
                    </option>

                    <option value="TEACHER">
                        Teacher
                    </option>

                    <option value="PARENT">
                        Parent
                    </option>

                    <option value="PUBLIC">
                        Public
                    </option>

                </select>

            </div>

            <div>

                <label>
                    Published At
                </label>

                <input
                    type="datetime-local"
                    name="published_at"
                    value={
                        formData.published_at || ''
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
                    Published By
                </label>

                <input
                    type="number"
                    name="published_by"
                    value={
                        formData.published_by || ''
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
                        name="is_published"
                        checked={
                            formData.is_published || false
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Published

                </label>

            </div>

        </div>

    );

};

export default TimetablePublicationForm;