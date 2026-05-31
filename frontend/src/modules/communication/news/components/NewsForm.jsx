const NewsForm = ({
    formData,
    setFormData,
}) => {

    return (
        <>
            <div className="mb-3">

                <label className="form-label">
                    News Title
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
                    Summary
                </label>

                <textarea
                    rows="3"
                    className="form-control"
                    value={
                        formData.summary || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            summary:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Content
                </label>

                <textarea
                    rows="8"
                    className="form-control"
                    value={
                        formData.content || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            content:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Published Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.published_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            published_date:
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
                        formData.is_published ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            is_published:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Published
                </label>

            </div>

        </>
    );
};

export default NewsForm;