const TimetableForm = ({
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
                    Academic Session
                </label>

                <input

                    type="number"

                    name="academic_session"

                    value={
                        formData.academic_session || ''
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
                    Bell Schedule
                </label>

                <input

                    type="number"

                    name="bell_schedule"

                    value={
                        formData.bell_schedule || ''
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

            <div>

                <label>
                    Effective To
                </label>

                <input

                    type="date"

                    name="effective_to"

                    value={
                        formData.effective_to || ''
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
                    Status
                </label>

                <select

                    name="status"

                    value={
                        formData.status || ''
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

                    <option value="DRAFT">
                        Draft
                    </option>

                    <option value="GENERATED">
                        Generated
                    </option>

                    <option value="APPROVED">
                        Approved
                    </option>

                    <option value="PUBLISHED">
                        Published
                    </option>

                </select>

            </div>

            <div
                className="
                    flex
                    items-center
                    mt-8
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

            <div
                className="
                    md:col-span-2
                "
            >

                <label>
                    Description
                </label>

                <textarea

                    name="description"

                    rows="4"

                    value={
                        formData.description || ''
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

export default TimetableForm;