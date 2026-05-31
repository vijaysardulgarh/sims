const NoticeForm = ({
    formData,
    setFormData,
}) => {

    return (
        <>
            <div className="mb-3">

                <label className="form-label">
                    Notice Number
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.notice_number || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            notice_number:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Title
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
                    rows="6"
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
                    Notice Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.notice_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            notice_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Expiry Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.expiry_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            expiry_date:
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

export default NoticeForm;