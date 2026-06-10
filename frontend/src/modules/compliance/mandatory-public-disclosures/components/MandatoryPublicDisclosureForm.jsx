const MandatoryPublicDisclosureForm = ({
    formData,
    setFormData,
}) => {

    const handleChange = (
        e
    ) => {

        setFormData({

            ...formData,

            [e.target.name]:
                e.target.value,

        });

    };

    return (

        <div
            className="
                grid
                grid-cols-2
                gap-6
            "
        >

            <div className="col-span-2">

                <h2
                    className="
                        text-lg
                        font-semibold
                    "
                >
                    General Information
                </h2>

            </div>

            <input
                type="text"
                name="affiliation_number"
                placeholder="Affiliation Number"
                value={
                    formData.affiliation_number || ""
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="text"
                name="school_code"
                placeholder="School Code"
                value={
                    formData.school_code || ""
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="text"
                name="principal_name"
                placeholder="Principal Name"
                value={
                    formData.principal_name || ""
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="text"
                name="principal_qualification"
                placeholder="Principal Qualification"
                value={
                    formData.principal_qualification || ""
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="email"
                name="school_email"
                placeholder="School Email"
                value={
                    formData.school_email || ""
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="text"
                name="contact_number"
                placeholder="Contact Number"
                value={
                    formData.contact_number || ""
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <div className="col-span-2">

                <h2
                    className="
                        text-lg
                        font-semibold
                        mt-4
                    "
                >
                    Staff Details
                </h2>

            </div>

            <input
                type="number"
                name="total_teachers"
                placeholder="Total Teachers"
                value={
                    formData.total_teachers || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="pgt_count"
                placeholder="PGT Count"
                value={
                    formData.pgt_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="tgt_count"
                placeholder="TGT Count"
                value={
                    formData.tgt_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="prt_count"
                placeholder="PRT Count"
                value={
                    formData.prt_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="dpe_count"
                placeholder="DPE Count"
                value={
                    formData.dpe_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="clerk_count"
                placeholder="Clerk Count"
                value={
                    formData.clerk_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="librarian_count"
                placeholder="Librarian Count"
                value={
                    formData.librarian_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="special_educator_count"
                placeholder="Special Educator Count"
                value={
                    formData.special_educator_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="number"
                name="counsellor_count"
                placeholder="Counsellor Count"
                value={
                    formData.counsellor_count || 0
                }
                onChange={handleChange}
                className="border p-3 rounded-lg"
            />

            <input
                type="text"
                name="student_teacher_ratio"
                placeholder="Student Teacher Ratio"
                value={
                    formData.student_teacher_ratio || ""
                }
                onChange={handleChange}
                className="
                    border
                    p-3
                    rounded-lg
                    col-span-2
                "
            />

        </div>

    );

};

export default MandatoryPublicDisclosureForm;