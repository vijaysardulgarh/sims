import {

    useEffect,

    useState

} from "react";


const AccessControlForm = ({

    initialData = null,

    onSubmit,

}) => {

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

    const handleSubmit = async (
        e
    ) => {

        e.preventDefault();

        await onSubmit(formData);
    };


    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            {/* NAME */}

            <div>

                <label className="block mb-1">

                    Name

                </label>

                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="border p-2 w-full rounded"
                    required
                />

            </div>


            {/* CODE */}

            <div>

                <label className="block mb-1">

                    Code

                </label>

                <input
                    type="text"
                    name="code"
                    value={formData.code}
                    onChange={handleChange}
                    className="border p-2 w-full rounded"
                    required
                />

            </div>


            {/* MODULE */}

            <div>

                <label className="block mb-1">

                    Module

                </label>

                <input
                    type="text"
                    name="module"
                    value={formData.module}
                    onChange={handleChange}
                    className="border p-2 w-full rounded"
                    required
                />

            </div>


            {/* DESCRIPTION */}

            <div>

                <label className="block mb-1">

                    Description

                </label>

                <textarea
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    className="border p-2 w-full rounded"
                    rows={4}
                />

            </div>


            {/* BUTTON */}

            <button
                type="submit"
                className="bg-blue-600 text-white px-4 py-2 rounded"
            >

                Save Access Control

            </button>

        </form>
    );
};

export default AccessControlForm;