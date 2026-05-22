import {

    useState

} from "react";


const UserRoleForm = ({

    initialData,

    users = [],

    roles = [],

    onSubmit,

}) => {

    const [formData, setFormData] =
        useState({

            user:
                initialData?.user
                    ? String(initialData.user)
                    : "",

            role:
                initialData?.role
                    ? String(initialData.role)
                    : "",
        });


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

        console.log(formData);

        await onSubmit(formData);
    };


    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >

            {/* USER */}

            <div>

                <label className="block mb-1">

                    User

                </label>

                <select
                    name="user"
                    value={formData.user}
                    onChange={handleChange}
                    className="border p-2 w-full"
                    required
                >

                    <option value="">

                        Select User

                    </option>

                    {
                        users.map((user) => (

                            <option
                                key={user.id}
                                value={String(user.id)}
                            >

                                {user.email}

                            </option>
                        ))
                    }

                </select>

            </div>


            {/* ROLE */}

            <div>

                <label className="block mb-1">

                    Role

                </label>

                <select
                    name="role"
                    value={formData.role}
                    onChange={handleChange}
                    className="border p-2 w-full"
                    required
                >

                    <option value="">

                        Select Role

                    </option>

                    {
                        roles.map((role) => (

                            <option
                                key={role.id}
                                value={String(role.id)}
                            >

                                {role.name}

                            </option>
                        ))
                    }

                </select>

            </div>


            {/* BUTTON */}

            <button
                type="submit"
                className="bg-blue-600 text-white px-4 py-2 rounded"
            >

                Save

            </button>

        </form>
    );
};

export default UserRoleForm;