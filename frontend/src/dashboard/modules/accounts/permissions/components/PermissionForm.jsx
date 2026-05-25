import {
    useEffect,
    useState
} from "react";


const PermissionForm = ({

    initialData = null,

    modules = [],

    onSubmit,

    loading = false,

}) => {

    // =====================================
    // STATE
    // =====================================

    const [formData, setFormData] = useState({

        module: "",

        action: "view",

        description: "",
    });


    // =====================================
    // ACTION OPTIONS
    // =====================================

    const actionOptions = [

        "view",

        "add",

        "edit",

        "delete",

        "import",

        "export",

        "assign",

        "approve",
    ];


    // =====================================
    // LOAD INITIAL DATA
    // =====================================

    useEffect(() => {

        if (
            initialData &&
            Object.keys(initialData).length > 0
        ) {

            setFormData({

                module:
                    initialData.module || "",

                action:
                    initialData.action || "view",

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
            {/* MODULE */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Module

                </label>

                <select
                    name="module"
                    value={formData.module}
                    onChange={handleChange}
                    className="border border-gray-300 p-2 w-full rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                >

                    <option value="">

                        Select Module

                    </option>

                    {modules.map((module) => (

                        <option
                            key={module.id}
                            value={module.id}
                        >

                            {module.name}

                        </option>

                    ))}

                </select>

            </div>


            {/* ================================= */}
            {/* ACTION */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Action

                </label>

                <select
                    name="action"
                    value={formData.action}
                    onChange={handleChange}
                    className="border border-gray-300 p-2 w-full rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                >

                    {actionOptions.map((action) => (

                        <option
                            key={action}
                            value={action}
                        >

                            {action}

                        </option>

                    ))}

                </select>

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
            {/* AUTO GENERATED INFO */}
            {/* ================================= */}

            <div className="bg-gray-50 p-4 rounded border">

                <p className="text-sm text-gray-600">

                    Permission name and code
                    will be generated automatically.

                </p>

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