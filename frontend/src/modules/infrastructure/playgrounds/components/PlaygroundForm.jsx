const PlaygroundForm = ({
    formData,
    setFormData,
}) => {

    return (
        <>
            <div className="mb-3">

                <label className="form-label">
                    Playground Name
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
                    Playground Type
                </label>

                <select
                    className="form-control"
                    value={
                        formData.playground_type ||
                        ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            playground_type:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Type
                    </option>

                    <option value="CRICKET">
                        Cricket Ground
                    </option>

                    <option value="FOOTBALL">
                        Football Ground
                    </option>

                    <option value="BASKETBALL">
                        Basketball Court
                    </option>

                    <option value="VOLLEYBALL">
                        Volleyball Court
                    </option>

                    <option value="BADMINTON">
                        Badminton Court
                    </option>

                    <option value="ATHLETICS">
                        Athletics Track
                    </option>

                    <option value="MULTIPURPOSE">
                        Multi Purpose Ground
                    </option>

                    <option value="OTHER">
                        Other
                    </option>

                </select>

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Area
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.area || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            area:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Capacity
                </label>

                <input
                    type="number"
                    className="form-control"
                    value={
                        formData.capacity || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            capacity:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Location
                </label>

                <input
                    type="text"
                    className="form-control"
                    value={
                        formData.location || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            location:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="form-check mb-2">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.covered ||
                        false
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            covered:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Covered
                </label>

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

export default PlaygroundForm;