const TimetableApprovalForm = ({
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
                        Select Status
                    </option>

                    <option value="DRAFT">
                        Draft
                    </option>

                    <option value="SUBMITTED">
                        Submitted
                    </option>

                    <option value="UNDER_REVIEW">
                        Under Review
                    </option>

                    <option value="APPROVED">
                        Approved
                    </option>

                    <option value="REJECTED">
                        Rejected
                    </option>

                </select>

            </div>

            <div>

                <label>
                    Approved By
                </label>

                <input
                    type="number"
                    name="approved_by"
                    value={
                        formData.approved_by || ''
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
                    Approved At
                </label>

                <input
                    type="datetime-local"
                    name="approved_at"
                    value={
                        formData.approved_at || ''
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

export default TimetableApprovalForm;