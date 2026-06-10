const AffiliationForm = ({
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
                <label>Board</label>

                <select
                    name="board"
                    value={formData.board || ""}
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                >
                    <option value="">Select</option>
                    <option value="CBSE">CBSE</option>
                    <option value="STATE">State Board</option>
                    <option value="ICSE">ICSE</option>
                    <option value="IB">IB</option>
                    <option value="CAMBRIDGE">Cambridge</option>
                </select>
            </div>

            <div>
                <label>Affiliation Number</label>

                <input
                    type="text"
                    name="affiliation_number"
                    value={
                        formData.affiliation_number || ""
                    }
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                />
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

            <div>
                <label>Status</label>

                <select
                    name="status"
                    value={
                        formData.status || "ACTIVE"
                    }
                    onChange={handleChange}
                    className="w-full border rounded-lg p-3"
                >
                    <option value="ACTIVE">Active</option>
                    <option value="EXPIRED">Expired</option>
                    <option value="PENDING">Pending</option>
                    <option value="SUSPENDED">Suspended</option>
                </select>
            </div>

            <div>
                <label>Affiliation Letter</label>

                <input
                    type="file"
                    onChange={(e) =>
                        setFormData({
                            ...formData,
                            affiliation_letter:
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

export default AffiliationForm;