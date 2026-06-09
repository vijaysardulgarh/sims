import {
    useEffect,
    useState,
} from "react";

import associationService from "../../associations/services/associationService";

const AssociationRoleForm = ({
    initialData = {},
    onSubmit,
}) => {

    const [associations,
        setAssociations] =
        useState([]);

    const [formData,
        setFormData] =
        useState({

            association:
                initialData.association || "",

            title:
                initialData.title || "",

            responsibilities:
                initialData.responsibilities || "",
        });

    // ========================================
    // LOAD ASSOCIATIONS
    // ========================================

    useEffect(() => {

        fetchAssociations();

    }, []);

    const fetchAssociations = async () => {

        try {

            const response =
                await associationService.getAssociations();

            setAssociations(

                response.data ||

                response ||

                []
            );

        } catch (error) {

            console.error(error);
        }
    };

    // ========================================
    // HANDLE CHANGE
    // ========================================

    const handleChange = (e) => {

        const {
            name,
            value,
        } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]: value,
        }));
    };

    // ========================================
    // SUBMIT
    // ========================================

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

            {/* ASSOCIATION */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >

                    Association

                </label>

                <select

                    name="association"

                    value={
                        formData.association
                    }

                    onChange={
                        handleChange
                    }

                    className="
                        w-full
                        border
                        rounded-lg
                        px-3
                        py-2
                    "

                    required
                >

                    <option value="">
                        Select Association
                    </option>

                    {
                        associations.map(
                            (association) => (

                                <option
                                    key={
                                        association.id
                                    }
                                    value={
                                        association.id
                                    }
                                >
                                    {
                                        association.name
                                    }
                                </option>

                            )
                        )
                    }

                </select>

            </div>

            {/* ROLE TITLE */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >

                    Role Title

                </label>

                <input

                    type="text"

                    name="title"

                    value={
                        formData.title
                    }

                    onChange={
                        handleChange
                    }

                    placeholder="Enter Role Title"

                    className="
                        w-full
                        border
                        rounded-lg
                        px-3
                        py-2
                    "

                    required
                />

            </div>

            {/* RESPONSIBILITIES */}

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >

                    Responsibilities

                </label>

                <textarea

                    name="responsibilities"

                    value={
                        formData.responsibilities
                    }

                    onChange={
                        handleChange
                    }

                    rows={5}

                    placeholder="Enter Responsibilities"

                    className="
                        w-full
                        border
                        rounded-lg
                        px-3
                        py-2
                    "
                />

            </div>

            {/* BUTTON */}

            <button

                type="submit"

                className="
                    bg-blue-600
                    text-white
                    px-5
                    py-2
                    rounded-lg
                "
            >

                Save

            </button>

        </form>
    );
};

export default AssociationRoleForm;