import {
    useEffect,
    useState
} from "react";

const PermissionForm = ({

    initialData = null,

    onSubmit,

    loading = false,

}) => {

    // =====================================
    // STATE
    // =====================================

    const [formData, setFormData] = useState({

        name: "",

        code: "",

        module: "",

        description: "",
    });


    // =====================================
    // LOAD INITIAL DATA
    // =====================================

    useEffect(() => {

        if (
            initialData &&
            Object.keys(initialData).length > 0
        ) {

            setFormData({

                name:
                    initialData.name || "",

                code:
                    initialData.code || "",

                module:
                    initialData.module || "",

                description:
                    initialData.description || "",
            });
        }

    }, [initialData]);


    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange = (e) => {

        const {
            name,
            value
        } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]: value,
        }));
    };


    // =====================================
    // HANDLE SUBMIT
    // =====================================

    const handleSubmit = async (e) => {

        e.preventDefault();

        if (!onSubmit) return;

        await onSubmit(formData);
    };


    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-5 bg-white p-6 rounded-lg shadow"
        >

            {/* ================================= */}
            {/* NAME */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Permission Name

                </label>

                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    placeholder="Enter permission name"
                    className="border border-gray-300 p-2 w-full rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />

            </div>


            {/* ================================= */}
            {/* CODE */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Permission Code

                </label>

                <input
                    type="text"
                    name="code"
                    value={formData.code}
                    onChange={handleChange}
                    placeholder="e.g. can_create_student"
                    className="border border-gray-300 p-2 w-full rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />

            </div>


            {/* ================================= */}
            {/* MODULE */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Module

                </label>

                <input
                    type="text"
                    name="module"
                    value={formData.module}
                    onChange={handleChange}
                    placeholder="e.g. students"
                    className="border border-gray-300 p-2 w-full rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />

            </div>


            {/* ================================= */}
            {/* DESCRIPTION */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Description

                </label>

                <textarea
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    rows={4}
                    placeholder="Enter permission description"
                    className="border border-gray-300 p-2 w-full rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                />

            </div>


            {/* ================================= */}
            {/* BUTTON */}
            {/* ================================= */}

            <div>

                <button
                    type="submit"
                    disabled={loading}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded transition disabled:opacity-50"
                >

                    {
                        loading
                            ? "Saving..."
                            : "Save Permission"
                    }

                </button>

            </div>

        </form>
    );
};

export default PermissionForm;