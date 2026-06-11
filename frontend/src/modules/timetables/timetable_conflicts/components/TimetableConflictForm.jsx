const TimetableConflictForm = ({
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
                    Conflict Type
                </label>

                <select

                    name="conflict_type"

                    value={
                        formData.conflict_type || ''
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

                    <option value="TEACHER">
                        Teacher Clash
                    </option>

                    <option value="ROOM">
                        Room Clash
                    </option>

                    <option value="RESOURCE">
                        Resource Clash
                    </option>

                    <option value="SUBJECT">
                        Subject Constraint
                    </option>

                </select>

            </div>

            <div>

                <label>
                    Severity
                </label>

                <select

                    name="severity"

                    value={
                        formData.severity || ''
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

                    <option value="LOW">
                        Low
                    </option>

                    <option value="MEDIUM">
                        Medium
                    </option>

                    <option value="HIGH">
                        High
                    </option>

                    <option value="CRITICAL">
                        Critical
                    </option>

                </select>

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

                    <option value="OPEN">
                        Open
                    </option>

                    <option value="RESOLVED">
                        Resolved
                    </option>

                    <option value="IGNORED">
                        Ignored
                    </option>

                </select>

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

                    rows="5"

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

export default TimetableConflictForm;