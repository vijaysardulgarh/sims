const EventForm = ({
    formData,
    setFormData,
}) => {

    return (
        <>
            <div className="mb-3">

                <label className="form-label">
                    Event Title
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.title || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            title:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Description
                </label>

                <textarea
                    rows="5"
                    className="form-control"
                    value={
                        formData.description || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            description:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Event Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.event_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            event_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Start Time
                </label>

                <input
                    type="time"
                    className="form-control"
                    value={
                        formData.start_time || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            start_time:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    End Time
                </label>

                <input
                    type="time"
                    className="form-control"
                    value={
                        formData.end_time || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            end_time:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Venue
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.venue || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            venue:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Organizer
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.organizer || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            organizer:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="form-check">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.is_active ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            is_active:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Active
                </label>

            </div>

        </>
    );
};

export default EventForm;