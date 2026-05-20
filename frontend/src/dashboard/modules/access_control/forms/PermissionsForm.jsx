import {
    useEffect,
    useState
} from "react";

import {
    useNavigate,
    useParams
} from "react-router-dom";

import permissionService from "../services/permissionService";


const PermissionForm = ({
    isEdit = false
}) => {

    const navigate =
        useNavigate();

    const { id } =
        useParams();


    // =====================================
    // STATE
    // =====================================

    const [loading,
        setLoading] =
        useState(false);

    const [formData,
        setFormData] =
        useState({

            name: "",

            code: "",

            module: "",

            description: "",

            is_active: true,
        });


    // =====================================
    // LOAD PERMISSION
    // =====================================

    useEffect(() => {

        if (isEdit && id) {

            fetchPermission();
        }

    }, [id]);


    // =====================================
    // FETCH PERMISSION
    // =====================================

    const fetchPermission =
        async () => {

        try {

            setLoading(true);

            const data =
                await permissionService.getPermission(
                    id
                );

            setFormData({

                name:
                    data.name || "",

                code:
                    data.code || "",

                module:
                    data.module || "",

                description:
                    data.description || "",

                is_active:
                    data.is_active ?? true,
            });

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange =
        (e) => {

        const {

            name,

            value,

            type,

            checked

        } = e.target;


        setFormData({

            ...formData,

            [name]:

                type === "checkbox"

                    ? checked

                    : value,
        });
    };


    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit =
        async (e) => {

        e.preventDefault();

        try {

            setLoading(true);

            if (isEdit) {

                await permissionService.updatePermission(

                    id,

                    formData
                );

            } else {

                await permissionService.createPermission(

                    formData
                );
            }

            navigate(
                "/dashboard/permissions"
            );

        } catch (error) {

            console.error(error);

            alert(
                "Failed to save permission"
            );

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // UI
    // =====================================

    return (

        <div
            className="
                bg-white
                rounded-2xl
                shadow-sm
                p-6
            "
        >

            {/* ================================= */}
            {/* HEADER */}
            {/* ================================= */}

            <div className="mb-6">

                <h2
                    className="
                        text-3xl
                        font-bold
                        text-gray-800
                    "
                >

                    {
                        isEdit
                            ? "Edit Permission"
                            : "Add Permission"
                    }

                </h2>

            </div>


            {/* ================================= */}
            {/* FORM */}
            {/* ================================= */}

            <form
                onSubmit={handleSubmit}
                className="space-y-5"
            >

                {/* NAME */}

                <div>

                    <label
                        className="
                            block
                            mb-2
                            font-medium
                        "
                    >

                        Name

                    </label>

                    <input

                        type="text"

                        name="name"

                        value={formData.name}

                        onChange={handleChange}

                        required

                        className="
                            w-full
                            border
                            rounded-xl
                            px-4
                            py-3
                        "
                    />

                </div>


                {/* CODE */}

                <div>

                    <label
                        className="
                            block
                            mb-2
                            font-medium
                        "
                    >

                        Code

                    </label>

                    <input

                        type="text"

                        name="code"

                        value={formData.code}

                        onChange={handleChange}

                        required

                        className="
                            w-full
                            border
                            rounded-xl
                            px-4
                            py-3
                        "
                    />

                </div>


                {/* MODULE */}

                <div>

                    <label
                        className="
                            block
                            mb-2
                            font-medium
                        "
                    >

                        Module

                    </label>

                    <input

                        type="text"

                        name="module"

                        value={formData.module}

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


                {/* DESCRIPTION */}

                <div>

                    <label
                        className="
                            block
                            mb-2
                            font-medium
                        "
                    >

                        Description

                    </label>

                    <textarea

                        name="description"

                        value={formData.description}

                        onChange={handleChange}

                        rows="4"

                        className="
                            w-full
                            border
                            rounded-xl
                            px-4
                            py-3
                        "
                    />

                </div>


                {/* ACTIVE */}

                <div
                    className="
                        flex
                        items-center
                        gap-3
                    "
                >

                    <input

                        type="checkbox"

                        name="is_active"

                        checked={formData.is_active}

                        onChange={handleChange}
                    />

                    <label>

                        Active

                    </label>

                </div>


                {/* BUTTON */}

                <div className="flex justify-end">

                    <button

                        type="submit"

                        disabled={loading}

                        className="
                            bg-blue-600
                            hover:bg-blue-700
                            text-white
                            px-6
                            py-3
                            rounded-xl
                            font-medium
                            transition
                        "
                    >

                        {
                            loading
                                ? "Saving..."
                                : "Save Permission"
                        }

                    </button>

                </div>

            </form>

        </div>
    );
};


export default PermissionForm;