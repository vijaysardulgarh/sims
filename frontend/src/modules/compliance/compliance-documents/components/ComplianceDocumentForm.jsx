const ComplianceDocumentForm = ({
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

            {/* DOCUMENT TYPE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                        text-gray-700
                    "
                >
                    Document Type
                </label>

                <select
                    name="document_type"
                    value={
                        formData.document_type || ""
                    }
                    onChange={
                        handleChange
                    }
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        p-3
                        focus:ring-2
                        focus:ring-blue-500
                        focus:border-blue-500
                    "
                >

                    <option value="">
                        Select Document Type
                    </option>

                    <option value="AFFILIATION_LETTER">
                        Affiliation Letter
                    </option>

                    <option value="NOC">
                        No Objection Certificate
                    </option>

                    <option value="RECOGNITION_CERTIFICATE">
                        Recognition Certificate
                    </option>

                    <option value="BUILDING_SAFETY">
                        Building Safety Certificate
                    </option>

                    <option value="FIRE_SAFETY">
                        Fire Safety Certificate
                    </option>

                    <option value="WATER_SANITATION">
                        Water & Sanitation Certificate
                    </option>

                    <option value="DEO_CERTIFICATE">
                        DEO Certificate
                    </option>

                    <option value="FEE_STRUCTURE">
                        Fee Structure
                    </option>

                    <option value="ACADEMIC_CALENDAR">
                        Academic Calendar
                    </option>

                    <option value="SMC_LIST">
                        School Management Committee
                    </option>

                    <option value="PTA_LIST">
                        Parent Teacher Association
                    </option>

                    <option value="BOARD_RESULTS">
                        Board Results
                    </option>

                </select>

            </div>

            {/* TITLE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                        text-gray-700
                    "
                >
                    Title
                </label>

                <input
                    type="text"
                    name="title"
                    value={
                        formData.title || ""
                    }
                    onChange={
                        handleChange
                    }
                    placeholder="Enter document title"
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        p-3
                        focus:ring-2
                        focus:ring-blue-500
                        focus:border-blue-500
                    "
                />

            </div>

            {/* ISSUE DATE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                        text-gray-700
                    "
                >
                    Issue Date
                </label>

                <input
                    type="date"
                    name="issue_date"
                    value={
                        formData.issue_date || ""
                    }
                    onChange={
                        handleChange
                    }
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        p-3
                        focus:ring-2
                        focus:ring-blue-500
                        focus:border-blue-500
                    "
                />

            </div>

            {/* EXPIRY DATE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                        text-gray-700
                    "
                >
                    Expiry Date
                </label>

                <input
                    type="date"
                    name="expiry_date"
                    value={
                        formData.expiry_date || ""
                    }
                    onChange={
                        handleChange
                    }
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        p-3
                        focus:ring-2
                        focus:ring-blue-500
                        focus:border-blue-500
                    "
                />

            </div>

            {/* ISSUING AUTHORITY */}

            <div
                className="
                    col-span-2
                "
            >

                <label
                    className="
                        block
                        mb-2
                        font-medium
                        text-gray-700
                    "
                >
                    Issuing Authority
                </label>

                <input
                    type="text"
                    name="issuing_authority"
                    value={
                        formData.issuing_authority || ""
                    }
                    onChange={
                        handleChange
                    }
                    placeholder="Enter issuing authority"
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        p-3
                        focus:ring-2
                        focus:ring-blue-500
                        focus:border-blue-500
                    "
                />

            </div>

            {/* DOCUMENT UPLOAD */}

            <div
                className="
                    col-span-2
                "
            >

                <label
                    className="
                        block
                        mb-2
                        font-medium
                        text-gray-700
                    "
                >
                    Document
                </label>

                <div
                    className="
                        border-2
                        border-dashed
                        border-gray-300
                        rounded-2xl
                        p-8
                        bg-gray-50
                        text-center
                        hover:border-blue-400
                        transition
                    "
                >

                    <input
                        type="file"
                        id="document-upload"
                        className="hidden"
                        onChange={(e) =>
                            setFormData({
                                ...formData,
                                document:
                                    e.target.files?.[0],
                            })
                        }
                    />

                    <label
                        htmlFor="document-upload"
                        className="
                            cursor-pointer
                            block
                        "
                    >

                        <div
                            className="
                                text-lg
                                font-semibold
                                text-gray-700
                            "
                        >
                            Upload Document
                        </div>

                        <div
                            className="
                                text-sm
                                text-gray-500
                                mt-1
                            "
                        >
                            PDF, DOC, DOCX
                        </div>

                        <div
                            className="
                                mt-4
                                inline-flex
                                items-center
                                px-5
                                py-2
                                bg-blue-600
                                text-white
                                rounded-lg
                                hover:bg-blue-700
                            "
                        >
                            Browse Files
                        </div>

                        {

                            formData.document && (

                                <div
                                    className="
                                        mt-4
                                        text-green-600
                                        font-medium
                                        break-all
                                    "
                                >

                                    Selected:
                                    {" "}
                                    {
                                        formData.document.name
                                    }

                                </div>

                            )

                        }

                    </label>

                </div>

            </div>

            {/* REMARKS */}

            <div
                className="
                    col-span-2
                "
            >

                <label
                    className="
                        block
                        mb-2
                        font-medium
                        text-gray-700
                    "
                >
                    Remarks
                </label>

                <textarea
                    rows="5"
                    name="remarks"
                    value={
                        formData.remarks || ""
                    }
                    onChange={
                        handleChange
                    }
                    placeholder="Enter remarks..."
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        p-3
                        focus:ring-2
                        focus:ring-blue-500
                        focus:border-blue-500
                    "
                />

            </div>

        </div>

    );

};

export default ComplianceDocumentForm;