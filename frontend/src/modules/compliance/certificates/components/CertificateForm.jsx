const CertificateForm = ({
    formData,
    setFormData,
}) => {

    const handleChange = (e) => {

        const {
            name,
            value,
        } = e.target;

        setFormData({
            ...formData,
            [name]: value,
        });

    };

    return (

        <div className="grid grid-cols-2 gap-6">

            <div>
                <label>Certificate Type</label>

                <select
                    name="certificate_type"
                    value={formData.certificate_type || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                >
                    <option value="">Select</option>
                    <option value="FIRE_SAFETY">Fire Safety</option>
                    <option value="BUILDING_SAFETY">Building Safety</option>
                    <option value="WATER_SANITATION">Water & Sanitation</option>
                    <option value="HEALTH">Health</option>
                    <option value="ELECTRICAL">Electrical</option>
                    <option value="STRUCTURAL">Structural</option>
                    <option value="LIFT_SAFETY">Lift Safety</option>
                    <option value="OTHER">Other</option>
                </select>
            </div>

            <div>
                <label>Certificate Number</label>

                <input
                    type="text"
                    name="certificate_number"
                    value={formData.certificate_number || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Issuing Authority</label>

                <input
                    type="text"
                    name="issuing_authority"
                    value={formData.issuing_authority || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Status</label>

                <select
                    name="status"
                    value={formData.status || "ACTIVE"}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                >
                    <option value="ACTIVE">Active</option>
                    <option value="EXPIRED">Expired</option>
                    <option value="PENDING">Pending</option>
                </select>
            </div>

            <div>
                <label>Issue Date</label>

                <input
                    type="date"
                    name="issue_date"
                    value={formData.issue_date || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Valid Upto</label>

                <input
                    type="date"
                    name="valid_upto"
                    value={formData.valid_upto || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div className="col-span-2">
                <label>Certificate Document</label>

                <input
                    type="file"
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            document:
                                e.target.files[0],
                        })
                    }
                />
            </div>

            <div className="col-span-2">
                <label>Remarks</label>

                <textarea
                    rows="4"
                    name="remarks"
                    value={formData.remarks || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

        </div>

    );

};

export default CertificateForm;