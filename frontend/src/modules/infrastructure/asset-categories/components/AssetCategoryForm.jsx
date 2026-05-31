const AssetCategoryForm = ({
    formData,
    setFormData,
}) => {

    return (
        <>
            <div className="mb-3">

                <label className="form-label">
                    Name
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.name || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            name:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Code
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.code || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            code:
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
                    rows="4"
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

export default AssetCategoryForm;