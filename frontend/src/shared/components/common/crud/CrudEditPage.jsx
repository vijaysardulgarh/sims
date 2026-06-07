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

    // ==========================================
    // LOAD RECORD
    // ==========================================

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

                } catch (error) {

                    console.error(
                        error
                    );

                    toast.error(
                        "Failed to load record."
                    );

                    navigate(
                        redirectPath
                    );

                } finally {

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

    // ==========================================
    // ERROR HANDLER
    // ==========================================

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

    // ==========================================
    // SUBMIT
    // ==========================================

    const handleSubmit =
        async (e) => {

            e.preventDefault();

            try {

                setSaving(
                    true
                );

                if (
                    method === "patch"
                ) {

                    await api.patch(
                        `${endpoint}${id}/`,
                        formData
                    );

                } else {

                    await api.put(
                        `${endpoint}${id}/`,
                        formData
                    );
                }

                toast.success(
                    successMessage
                );

                navigate(
                    redirectPath
                );

            } catch (error) {

                console.error(
                    error
                );

                handleApiErrors(
                    error
                );

            } finally {

                setSaving(
                    false
                );
            }
        };

    // ==========================================
    // LOADING
    // ==========================================

    if (loading) {

        return (

            <div
                className="
                    container-fluid
                    py-4
                "
            >

                <div
                    className="
                        card
                        shadow-sm
                    "
                >

                    <div
                        className="
                            card-body
                            text-center
                        "
                    >

                        Loading...

                    </div>

                </div>

            </div>
        );
    }

    // ==========================================
    // PAGE
    // ==========================================

    return (

        <div
            className="
                container-fluid
            "
        >

            <div
                className="
                    d-flex
                    justify-content-between
                    align-items-center
                    mb-4
                "
            >

                <h3
                    className="
                        mb-0
                    "
                >
                    {title}
                </h3>

                <button
                    type="button"
                    className="
                        btn
                        btn-outline-secondary
                    "
                    onClick={() =>
                        navigate(
                            redirectPath
                        )
                    }
                >
                    Back
                </button>

            </div>

            <div
                className="
                    card
                    shadow-sm
                    border-0
                "
            >

                <div
                    className="
                        card-body
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
                                d-flex
                                gap-2
                                mt-4
                            "
                        >

                            <button

                                type="submit"

                                disabled={
                                    saving
                                }

                                className="
                                    btn
                                    btn-primary
                                "
                            >

                                {saving
                                    ? "Updating..."
                                    : "Update"}

                            </button>

                            <button

                                type="button"

                                disabled={
                                    saving
                                }

                                className="
                                    btn
                                    btn-light
                                "

                                onClick={() =>
                                    navigate(
                                        redirectPath
                                    )
                                }

                            >

                                Cancel

                            </button>

                        </div>

                    </form>

                </div>

            </div>

        </div>

    );
};

export default CrudEditPage;