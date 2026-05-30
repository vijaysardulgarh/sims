import {
    useState,
    useEffect
} from "react";

const SMCMemberForm = ({
    initialData = {},
    onSubmit,
    loading = false,
}) => {

    // =====================================
    // STATE
    // =====================================

    const [formData, setFormData] =
        useState({

            name: "",

            position: "President",

            gender: "",

            category: "",

            contact_number: "",

            email: "",

            address: "",

            nomination_date: "",

            tenure_end_date: "",

            photo: null,

            priority: 0,

            show_on_website: true,

            remarks: "",

        });

    const [errors, setErrors] =
        useState({});

    // =====================================
    // LOAD INITIAL DATA
    // =====================================

    useEffect(() => {

        if (
            initialData &&
            Object.keys(initialData).length > 0
        ) {

            setFormData((prev) => ({

                ...prev,

                ...initialData,

                photo: null,

            }));

        }

    }, [initialData]);

    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked,
            files,
        } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]:
                type === "checkbox"
                    ? checked
                    : type === "file"
                        ? files[0]
                        : value,

        }));

    };

    // =====================================
    // VALIDATION
    // =====================================

    const validate = () => {

        const newErrors = {};

        if (!formData.name?.trim()) {

            newErrors.name =
                "Name is required";

        }

        if (!formData.position) {

            newErrors.position =
                "Position is required";

        }

        if (
            formData.email &&
            !/\S+@\S+\.\S+/.test(
                formData.email
            )
        ) {

            newErrors.email =
                "Enter a valid email";

        }

        setErrors(newErrors);

        return (
            Object.keys(newErrors)
                .length === 0
        );

    };

    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit = (e) => {

        e.preventDefault();

        if (!validate()) {

            return;

        }

        onSubmit(formData);

    };

    // =====================================
    // UI
    // =====================================

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-6"
        >

            <div className="
                bg-white
                rounded-2xl
                shadow
                p-6
            ">

                <h2 className="
                    text-2xl
                    font-bold
                    mb-6
                ">
                    SMC Member Information
                </h2>

                <div className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                ">

                    {/* NAME */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Name *
                        </label>

                        <input
                            type="text"
                            name="name"
                            value={formData.name}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                        {
                            errors.name && (

                                <p className="
                                    text-red-500
                                    text-sm
                                    mt-1
                                ">
                                    {errors.name}
                                </p>

                            )
                        }

                    </div>

                    {/* POSITION */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Position *
                        </label>

                        <select
                            name="position"
                            value={formData.position}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        >

                            <option value="President">
                                President
                            </option>

                            <option value="Vice President">
                                Vice President
                            </option>

                            <option value="Member (Secretary)">
                                Member (Secretary)
                            </option>

                            <option value="Member (Trained Education Scholar)">
                                Member (Trained Education Scholar)
                            </option>

                            <option value="Member (Teacher/Student)">
                                Member (Teacher/Student)
                            </option>

                            <option value="Member (Parent/Guardian)">
                                Member (Parent/Guardian)
                            </option>

                            <option value="Member (General)">
                                Member (General)
                            </option>

                        </select>

                    </div>

                    {/* GENDER */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Gender
                        </label>

                        <select
                            name="gender"
                            value={formData.gender || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        >

                            <option value="">
                                Select Gender
                            </option>

                            <option value="Male">
                                Male
                            </option>

                            <option value="Female">
                                Female
                            </option>

                            <option value="Other">
                                Other
                            </option>

                        </select>

                    </div>

                    {/* CATEGORY */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Category
                        </label>

                        <select
                            name="category"
                            value={formData.category || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        >

                            <option value="">
                                Select Category
                            </option>

                            <option value="GEN">
                                General
                            </option>

                            <option value="SC">
                                Scheduled Caste
                            </option>

                            <option value="BC-A">
                                Backward Class - A
                            </option>

                            <option value="BC-B">
                                Backward Class - B
                            </option>

                            <option value="EWS">
                                Economically Weaker Section
                            </option>

                            <option value="OTHER">
                                Other
                            </option>

                        </select>

                    </div>

                    {/* CONTACT */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Contact Number
                        </label>

                        <input
                            type="text"
                            name="contact_number"
                            value={formData.contact_number || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                    {/* EMAIL */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Email
                        </label>

                        <input
                            type="email"
                            name="email"
                            value={formData.email || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                    {/* ADDRESS */}

                    <div className="md:col-span-2">

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Address
                        </label>

                        <textarea
                            name="address"
                            rows="3"
                            value={formData.address || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                    {/* NOMINATION DATE */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Nomination Date
                        </label>

                        <input
                            type="date"
                            name="nomination_date"
                            value={formData.nomination_date || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                    {/* TENURE END DATE */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Tenure End Date
                        </label>

                        <input
                            type="date"
                            name="tenure_end_date"
                            value={formData.tenure_end_date || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                    {/* PHOTO */}

                    <div className="md:col-span-2">

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Photo
                        </label>

                        <input
                            type="file"
                            name="photo"
                            accept="image/*"
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                    {/* PRIORITY */}

                    <div>

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Priority
                        </label>

                        <input
                            type="number"
                            min="0"
                            name="priority"
                            value={formData.priority}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                    {/* SHOW ON WEBSITE */}

                    <div className="
                        flex
                        items-center
                        gap-3
                        pt-8
                    ">

                        <input
                            type="checkbox"
                            name="show_on_website"
                            checked={
                                formData.show_on_website
                            }
                            onChange={handleChange}
                        />

                        <label>
                            Show On Website
                        </label>

                    </div>

                    {/* REMARKS */}

                    <div className="md:col-span-2">

                        <label className="
                            block
                            mb-2
                            font-medium
                        ">
                            Remarks
                        </label>

                        <textarea
                            name="remarks"
                            rows="4"
                            value={formData.remarks || ""}
                            onChange={handleChange}
                            className="
                                w-full
                                border
                                rounded-xl
                                px-4
                                py-3
                            "
                        />

                    </div>

                </div>

            </div>

            <button
                type="submit"
                disabled={loading}
                className="
                    bg-blue-600
                    hover:bg-blue-700
                    text-white
                    px-8
                    py-3
                    rounded-xl
                    font-semibold
                    disabled:opacity-50
                "
            >

                {
                    loading
                        ? "Saving..."
                        : "Save SMC Member"
                }

            </button>

        </form>

    );

};

export default SMCMemberForm;