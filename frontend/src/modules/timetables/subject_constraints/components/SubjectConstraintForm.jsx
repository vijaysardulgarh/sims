const SubjectConstraintForm = ({
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
                    Constraint Type
                </label>

                <select

                    name="constraint_type"

                    value={
                        formData.constraint_type || ''
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

                    <option value="MAX_PER_DAY">
                        Max Per Day
                    </option>

                    <option value="MIN_PER_WEEK">
                        Min Per Week
                    </option>

                    <option value="CONSECUTIVE">
                        Consecutive Required
                    </option>

                    <option value="LAB">
                        Lab Required
                    </option>

                </select>

            </div>

            <div>

                <label>
                    Value
                </label>

                <input
                    type="text"
                    name="value"
                    value={
                        formData.value || ''
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

                <label
                    className="
                        flex
                        items-center
                        gap-3
                        mt-8
                    "
                >

                    <input
                        type="checkbox"
                        name="is_mandatory"
                        checked={
                            formData.is_mandatory || false
                        }
                        onChange={
                            handleChange
                        }
                    />

                    Mandatory Constraint

                </label>

            </div>

        </div>

    );

};

export default SubjectConstraintForm;