const TimetableForm = ({
    formData,
    setFormData,
    academicSessions = [],
    bellSchedules = [],
    classes = [],
    sections = [],
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

        if (
            name ===
            "school_class"
        ) {

            setFormData({

                ...formData,

                school_class:
                    value,

                section: "",

            });

            return;

        }

        setFormData({

            ...formData,

            [name]:

                type === "checkbox"

                    ? checked

                    : value,

        });

    };

    const filteredSections =

        sections.filter(
            section =>

                String(
                    section.class_obj
                )

                ===

                String(
                    formData.school_class
                )
        );

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
                    value={formData.name || ""}
                    onChange={handleChange}
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
                    value={formData.code || ""}
                    onChange={handleChange}
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

                <select
                    name="academic_session"
                    value={
                        formData.academic_session
                        || ""
                    }
                    onChange={handleChange}
                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Session
                    </option>

                    {academicSessions.map(
                        item => (

                            <option
                                key={item.id}
                                value={item.id}
                            >

                                {
                                    item.name
                                    ||
                                    item.title
                                    ||
                                    item.session_name
                                }

                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label>
                    Bell Schedule
                </label>

                <select
                    name="bell_schedule"
                    value={
                        formData.bell_schedule
                        || ""
                    }
                    onChange={handleChange}
                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Bell Schedule
                    </option>

                    {bellSchedules.map(
                        item => (

                            <option
                                key={item.id}
                                value={item.id}
                            >

                                {
                                    item.name
                                    ||
                                    item.title
                                }

                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label>
                    Class
                </label>

                <select
                    name="school_class"
                    value={
                        formData.school_class
                        || ""
                    }
                    onChange={handleChange}
                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Class
                    </option>

                    {classes.map(
                        item => (

                            <option
                                key={item.id}
                                value={item.id}
                            >

                                {
                                    item.name
                                }

                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label>
                    Section
                </label>

                <select
                    name="section"
                    value={
                        formData.section
                        || ""
                    }
                    onChange={handleChange}
                    className="
                        w-full
                        border
                        rounded-xl
                        px-4
                        py-3
                    "
                >

                    <option value="">
                        Select Section
                    </option>

                    {filteredSections.map(
                        item => (

                            <option
                                key={item.id}
                                value={item.id}
                            >

                                {
                                    item.name
                                }

                            </option>

                        )
                    )}

                </select>

            </div>

            <div>

                <label>
                    Effective From
                </label>

                <input
                    type="date"
                    name="effective_from"
                    value={
                        formData.effective_from
                        || ""
                    }
                    onChange={handleChange}
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
                        formData.effective_to
                        || ""
                    }
                    onChange={handleChange}
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
                            formData.is_published
                            || false
                        }
                        onChange={handleChange}
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
                    Remarks
                </label>

                <textarea
                    name="remarks"
                    rows="4"
                    value={
                        formData.remarks
                        || ""
                    }
                    onChange={handleChange}
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