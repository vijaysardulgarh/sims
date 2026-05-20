import {
    useState
} from "react";


const RoleForm = ({
    isEdit = false
}) => {

    const [formData,
        setFormData] = useState({

            name: "",

            code: "",

            description: "",
        });


    // =====================================
    // HANDLE CHANGE
    // =====================================

    const handleChange = (
        e
    ) => {

        setFormData({

            ...formData,

            [e.target.name]:
                e.target.value,
        });
    };


    // =====================================
    // SUBMIT
    // =====================================

    const handleSubmit = (
        e
    ) => {

        e.preventDefault();

        console.log(formData);
    };


    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            <input
                type="text"
                name="name"
                placeholder="Role Name"
                value={formData.name}
                onChange={handleChange}
            />

            <input
                type="text"
                name="code"
                placeholder="Role Code"
                value={formData.code}
                onChange={handleChange}
            />

            <textarea
                name="description"
                placeholder="Description"
                value={formData.description}
                onChange={handleChange}
            />

            <button type="submit">

                {
                    isEdit
                        ? "Update Role"
                        : "Create Role"
                }

            </button>

        </form>
    );
};

export default RoleForm;