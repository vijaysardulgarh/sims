import {
    useState,
} from "react";

import {
    useNavigate,
} from "react-router-dom";

import toast from "react-hot-toast";

import api from "../../../../services/api/axios";

const CrudCreatePage = ({
    title,
    endpoint,
    FormComponent,
    redirectPath,
    successMessage = "Record created successfully.",
}) => {

    const navigate =
        useNavigate();

    const [formData, setFormData] =
        useState({});

    const [saving, setSaving] =
        useState(false);

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
    // CREATE
    // ==========================================

    const handleSubmit =
        async (e) => {

            e.preventDefault();

            try {

                setSaving(
                    true
                );

                await api.post(
                    endpoint,
                    formData
                );

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
                                    ? "Saving..."
                                    : "Save"}

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

export default CrudCreatePage;