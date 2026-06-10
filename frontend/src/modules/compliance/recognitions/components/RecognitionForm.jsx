const RecognitionForm = ({
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
                <label>Recognition Type</label>

                <select
                    name="recognition_type"
                    value={formData.recognition_type || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                >
                    <option value="">Select</option>
                    <option value="SCHOOL_RECOGNITION">
                        School Recognition
                    </option>
                    <option value="RTE_RECOGNITION">
                        RTE Recognition
                    </option>
                    <option value="GOVERNMENT_APPROVAL">
                        Government Approval
                    </option>
                    <option value="MINORITY_STATUS">
                        Minority Status
                    </option>
                    <option value="OTHER">
                        Other
                    </option>
                </select>
            </div>

            <div>
                <label>Recognition Number</label>

                <input
                    type="text"
                    name="recognition_number"
                    value={
                        formData.recognition_number || ""
                    }
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
            </div>

            <div>
                <label>Issuing Authority</label>

                <input
                    type="text"
                    name="issuing_authority"
                    value={
                        formData.issuing_authority || ""
                    }
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
                <label>Recognition Document</label>

                <input
                    type="file"
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            recognition_document:
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

export default RecognitionForm;