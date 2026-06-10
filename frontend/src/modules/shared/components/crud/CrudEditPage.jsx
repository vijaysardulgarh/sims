import {
    useEffect,
    useState,
    useCallback,
} from "react";

import {
    useNavigate,
    useParams,
} from "react-router-dom";

import toast from "react-hot-toast";

import api from "../../../../services/api/axios";

const CrudEditPage = ({
    title,
    endpoint,
    FormComponent,
    redirectPath,
    successMessage = "Record updated successfully.",
    method = "put",
}) => {

    const { id } =
        useParams();

    const navigate =
        useNavigate();

    const [formData, setFormData] =
        useState({});

    const [loading, setLoading] =
        useState(true);

    const [saving, setSaving] =
        useState(false);

    const loadRecord =
        useCallback(
            async () => {

                try {

                    setLoading(
                        true
                    );

                    const response =
                        await api.get(
                            `${endpoint}${id}/`
                        );

                    setFormData(
                        response.data
                    );

                }

                catch (error) {

                    console.error(
                        error
                    );

                    toast.error(
                        "Failed to load record."
                    );

                    navigate(
                        redirectPath
                    );

                }

                finally {

                    setLoading(
                        false
                    );

                }

            },
            [
                endpoint,
                id,
                navigate,
                redirectPath,
            ]
        );

    useEffect(() => {

        loadRecord();

    }, [loadRecord]);

    const handleApiErrors = (
        error
    ) => {

        const errors =
            error.response?.data;

        if (!errors) {

            toast.error(
                "Something went wrong."
            );

            return;

        }

        Object.entries(
            errors
        ).forEach(
            ([field, messages]) => {

                const value =
                    Array.isArray(
                        messages
                    )
                        ? messages.join(
                              ", "
                          )
                        : messages;

                toast.error(
                    `${field}: ${value}`
                );

            }
        );

    };

    const handleSubmit =
        async (e) => {

            e.preventDefault();

            try {

                setSaving(
                    true
                );

                const hasFile =

                    Object.values(
                        formData
                    ).some(
                        value =>
                            value instanceof File
                    );

                if (hasFile) {

                    const payload =
                        new FormData();

                    Object.entries(
                        formData
                    ).forEach(
                        ([key, value]) => {

                            if (

                                value === null ||

                                value === undefined ||

                                value === ""

                            ) {

                                return;

                            }

                            if (

                                typeof value === "string" &&

                                (
                                    value.startsWith(
                                        "http://"
                                    ) ||

                                    value.startsWith(
                                        "https://"
                                    )
                                )

                            ) {

                                return;

                            }

                            payload.append(
                                key,
                                value
                            );

                        }
                    );

                    console.log(
                        formData
                    );


                    if (
                        method === "patch"
                    ) {

                        await api.patch(

                            `${endpoint}${id}/`,

                            payload,

                            {
                                headers: {
                                    "Content-Type":
                                        "multipart/form-data",
                                },
                            }

                        );

                    }

                    else {

                        await api.put(

                            `${endpoint}${id}/`,

                            payload,

                            {
                                headers: {
                                    "Content-Type":
                                        "multipart/form-data",
                                },
                            }

                        );

                    }

                }

                else {

                    if (
                        method === "patch"
                    ) {

                        await api.patch(
                            `${endpoint}${id}/`,
                            formData
                        );

                    }

                    else {

                        await api.put(
                            `${endpoint}${id}/`,
                            formData
                        );

                    }

                }

                toast.success(
                    successMessage
                );

                navigate(
                    redirectPath
                );

            }

            catch (error) {

                console.error(
                    error
                );

                handleApiErrors(
                    error
                );

            }

            finally {

                setSaving(
                    false
                );

            }

        };

    if (loading) {

        return (

            <div
                className="
                    max-w-5xl
                    mx-auto
                    py-10
                "
            >

                <div
                    className="
                        bg-white
                        rounded-2xl
                        shadow
                        p-10
                        text-center
                    "
                >

                    Loading...

                </div>

            </div>

        );

    }

    return (

        <div
            className="
                max-w-5xl
                mx-auto
                space-y-6
            "
        >

            <div
                className="
                    flex
                    items-center
                    justify-between
                "
            >

                <div>

                    <h1
                        className="
                            text-3xl
                            font-bold
                            text-gray-900
                        "
                    >
                        {title}
                    </h1>

                    <p
                        className="
                            text-gray-500
                            mt-1
                        "
                    >
                        Update existing record
                    </p>

                </div>

                <button

                    type="button"

                    onClick={() =>
                        navigate(
                            redirectPath
                        )
                    }

                    className="
                        px-4
                        py-2
                        border
                        border-gray-300
                        rounded-xl
                        hover:bg-gray-100
                        transition
                    "
                >

                    Back

                </button>

            </div>

            <div
                className="
                    bg-white
                    rounded-2xl
                    shadow
                    p-8
                "
            >

                <form
                    onSubmit={
                        handleSubmit
                    }
                >

                    <FormComponent

                        formData={
                            formData
                        }

                        setFormData={
                            setFormData
                        }

                        loading={
                            saving
                        }

                    />

                    <div
                        className="
                            flex
                            gap-3
                            mt-8
                        "
                    >

                        <button

                            type="submit"

                            disabled={
                                saving
                            }

                            className="
                                px-6
                                py-3
                                bg-blue-600
                                text-white
                                rounded-xl
                                hover:bg-blue-700
                                disabled:opacity-50
                            "
                        >

                            {
                                saving
                                    ? "Updating..."
                                    : "Update"
                            }

                        </button>

                        <button

                            type="button"

                            disabled={
                                saving
                            }

                            onClick={() =>
                                navigate(
                                    redirectPath
                                )
                            }

                            className="
                                px-6
                                py-3
                                border
                                border-gray-300
                                rounded-xl
                                hover:bg-gray-100
                            "
                        >

                            Cancel

                        </button>

                    </div>

                </form>

            </div>

        </div>

    );

};

export default CrudEditPage;