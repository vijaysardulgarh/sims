const FacilityForm = ({
    formData,
    setFormData,
}) => {

    return (
        <>
            <div className="mb-3">

                <label className="form-label">
                    Facility Name
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
                    Facility Type
                </label>

                <select
                    className="form-control"
                    value={
                        formData.facility_type || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            facility_type:
                                e.target.value,
                        })
                    }
                >
                    <option value="">
                        Select Type
                    </option>

                    <option value="CCTV">
                        CCTV
                    </option>

                    <option value="WIFI">
                        WiFi
                    </option>

                    <option value="RO_WATER">
                        RO Water
                    </option>

                    <option value="MEDICAL_ROOM">
                        Medical Room
                    </option>

                    <option value="TRANSPORT">
                        Transport
                    </option>

                    <option value="HOSTEL">
                        Hostel
                    </option>

                    <option value="POWER_BACKUP">
                        Power Backup
                    </option>

                    <option value="BIOMETRIC">
                        Biometric System
                    </option>

                    <option value="PA_SYSTEM">
                        Public Address System
                    </option>

                    <option value="OTHER">
                        Other
                    </option>

                </select>

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

            <div className="mb-3">

                <label className="form-label">
                    Installation Date
                </label>

                <input
                    type="date"
                    className="form-control"
                    value={
                        formData.installation_date || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            installation_date:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="mb-3">

                <label className="form-label">
                    Remarks
                </label>

                <textarea
                    rows="3"
                    className="form-control"
                    value={
                        formData.remarks || ''
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            remarks:
                                e.target.value,
                        })
                    }
                />

            </div>

            <div className="form-check mb-3">

                <input
                    type="checkbox"
                    className="form-check-input"
                    checked={
                        formData.available ??
                        true
                    }
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            available:
                                e.target.checked,
                        })
                    }
                />

                <label className="form-check-label">
                    Available
                </label>

            </div>
        </>
    );
};

export default FacilityForm;