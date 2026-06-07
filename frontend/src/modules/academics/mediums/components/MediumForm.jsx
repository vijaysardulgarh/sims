import {
    useState,
    useEffect
} from "react";

const AcademicSessionForm = ({

    initialData = {},

    onSubmit,

    loading = false,

}) => {

    // ============================================
    // FORM STATE
    // ============================================

    const [formData, setFormData] =
        useState({

            name: "",

            start_date: "",

            end_date: "",

            is_current: false,

        });

    // ============================================
    // PREFILL FORM
    // ============================================

    useEffect(() => {

        if (
            initialData &&
            Object.keys(initialData).length > 0
        ) {

            setFormData({

                name:
                    initialData.name || "",

                start_date:
                    initialData.start_date || "",

                end_date:
                    initialData.end_date || "",

                is_current:
                    initialData.is_current || false,

            });
        }

    }, [initialData]);

    // ============================================
    // HANDLE CHANGE
    // ============================================

    const handleChange = (e) => {

        const {
            name,
            value,
            type,
            checked,
        } = e.target;

        setFormData({

            ...formData,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,

        });
    };

    // ============================================
    // HANDLE SUBMIT
    // ============================================

    const handleSubmit = (e) => {

        e.preventDefault();

        onSubmit(formData);
    };

    return (

        <form
            onSubmit={handleSubmit}
            className="
                bg-white
                p-6
                rounded-2xl
                shadow
                space-y-6
            "
        >

            {/* SESSION NAME */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Session Name
                </label>

                <input

                    type="text"

                    name="name"

                    value={formData.name}

                    onChange={handleChange}

                    placeholder="2025-2026"

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "

                    required

                />

            </div>

            {/* START DATE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    Start Date
                </label>

                <input

                    type="date"

                    name="start_date"

                    value={
                        formData.start_date
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "

                    required

                />

            </div>

            {/* END DATE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        text-sm
                        font-medium
                    "
                >
                    End Date
                </label>

                <input

                    type="date"

                    name="end_date"

                    value={
                        formData.end_date
                    }

                    onChange={
                        handleChange
                    }

                    min={
                        formData.start_date
                    }

                    className="
                        w-full
                        border
                        rounded-lg
                        p-3
                    "

                    required

                />

            </div>

            {/* CURRENT SESSION */}

            <div>

                <label
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input

                        type="checkbox"

                        name="is_current"

                        checked={
                            formData.is_current
                        }

                        onChange={
                            handleChange
                        }

                        className="
                            h-4
                            w-4
                        "

                    />

                    <span
                        className="
                            text-sm
                            font-medium
                        "
                    >
                        Set as Current Academic Session
                    </span>

                </label>

            </div>

            {/* BUTTON */}

            <button

                type="submit"

                disabled={loading}

                className="
                    bg-blue-600
                    text-white
                    px-6
                    py-3
                    rounded-xl
                    hover:bg-blue-700
                    disabled:opacity-50
                "
            >

                {loading
                    ? "Saving..."
                    : initialData?.id
                        ? "Update Session"
                        : "Save Session"}

            </button>

        </form>

    );
};

export default AcademicSessionForm;