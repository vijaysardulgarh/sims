const InspectionForm = ({
    formData,
    setFormData,
}) => {

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]:
                e.target.value,
        });

    };

    return (

        <div className="grid grid-cols-2 gap-6">

            <div>
                <label>Inspection Type</label>

                <select
                    name="inspection_type"
                    value={formData.inspection_type || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                >
                    <option value="">Select</option>
                    <option value="CBSE">CBSE</option>
                    <option value="EDUCATION_DEPARTMENT">
                        Education Department
                    </option>
                    <option value="FIRE">Fire</option>
                    <option value="HEALTH">Health</option>
                    <option value="BUILDING">Building</option>
                    <option value="WATER_SANITATION">
                        Water & Sanitation
                    </option>
                    <option value="OTHER">Other</option>
                </select>
            </div>

            <div>
                <label>Inspection Date</label>

                <input
                    type="date"
                    name="inspection_date"
                    value={formData.inspection_date || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Authority</label>

                <input
                    type="text"
                    name="authority"
                    value={formData.authority || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Officer Name</label>

                <input
                    type="text"
                    name="officer_name"
                    value={formData.officer_name || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Report Number</label>

                <input
                    type="text"
                    name="report_number"
                    value={formData.report_number || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Status</label>

                <select
                    name="status"
                    value={formData.status || "PASSED"}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                >
                    <option value="PASSED">Passed</option>
                    <option value="FAILED">Failed</option>
                    <option value="PENDING">Pending</option>
                    <option value="CONDITIONAL">
                        Conditional Approval
                    </option>
                </select>
            </div>

            <div className="col-span-2">
                <label>Inspection Report</label>

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

export default InspectionForm;