import {

    useEffect,

    useState

} from "react";


const RoleForm = ({

    initialData = null,

    onSubmit,

}) => {

    // =====================================
    // STATE
    // =====================================

    const [formData, setFormData] = useState({

        name: "",

        code: "",

        description: "",

        is_active: true,
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

                description:
                    initialData.description || "",

                is_active:
                    initialData.is_active ?? true,
            });
        }

    }, [initialData]);


    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange = (e) => {

        const {

            name,

            value,

            checked,

            type

        } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        }));
    };


    // =====================================
    // HANDLE SUBMIT
    // =====================================

    const handleSubmit = async (
        e
    ) => {

        e.preventDefault();

        console.log(
            "Submitting Form:",
            formData
        );

        await onSubmit(formData);
    };


    // =====================================
    // UI
    // =====================================

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            {/* ================================= */}
            {/* NAME */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Name

                </label>

                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="border border-gray-300 p-2 w-full rounded"
                    required
                />

            </div>


            {/* ================================= */}
            {/* CODE */}
            {/* ================================= */}

            <div>

                <label className="block mb-1 font-medium">

                    Code

                </label>

                <input
                    type="text"
                    name="code"
                    value={formData.code}
                    onChange={handleChange}
                    className="border border-gray-300 p-2 w-full rounded"
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
                    className="border border-gray-300 p-2 w-full rounded"
                    rows={4}
                />

            </div>


            {/* ================================= */}
            {/* ACTIVE */}
            {/* ================================= */}

            <div className="flex items-center gap-2">

                <input
                    type="checkbox"
                    name="is_active"
                    checked={formData.is_active}
                    onChange={handleChange}
                />

                <label className="font-medium">

                    Active

                </label>

            </div>


            {/* ================================= */}
            {/* SUBMIT BUTTON */}
            {/* ================================= */}

            <button
                type="submit"
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
            >

                Save Role

            </button>

        </form>
    );
};

export default RoleForm;