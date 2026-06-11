const RoomAllocationForm = ({
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
                    Timetable Entry
                </label>

                <input
                    type="number"
                    name="timetable_entry"
                    value={
                        formData.timetable_entry || ''
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
                    Allocation Date
                </label>

                <input
                    type="date"
                    name="allocation_date"
                    value={
                        formData.allocation_date || ''
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

export default RoomAllocationForm;