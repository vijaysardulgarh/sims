import {
    useEffect,
    useState
} from "react";

import {
    useNavigate
} from "react-router-dom";

import userService
from "../services/userService";


const UserForm = ({
    userId = null
}) => {

    const navigate =
        useNavigate();


    // =====================================
    // STATE
    // =====================================

    const [formData,
        setFormData] =
        useState({

            first_name: "",

            last_name: "",

            email: "",

            phone: "",

            designation: "",

            password: "",

            profile_photo: null,

            is_active: true,

            is_staff: false,

            is_superuser: false,

            is_email_verified: false,

            is_phone_verified: false,
        });

    const [preview,
        setPreview] =
        useState(null);

    const [loading,
        setLoading] =
        useState(false);


    // =====================================
    // LOAD USER
    // =====================================

    useEffect(() => {

        if (userId) {

            fetchUser();
        }

    }, [userId]);


    const fetchUser =
        async () => {

        try {

            const data =
                await userService.getUser(
                    userId
                );

            setFormData({

                first_name:
                    data.first_name || "",

                last_name:
                    data.last_name || "",

                email:
                    data.email || "",

                phone:
                    data.phone || "",

                designation:
                    data.designation || "",

                password: "",

                profile_photo: null,

                is_active:
                    data.is_active ?? true,

                is_staff:
                    data.is_staff ?? false,

                is_superuser:
                    data.is_superuser ?? false,

                is_email_verified:
                    data.is_email_verified ?? false,

                is_phone_verified:
                    data.is_phone_verified ?? false,
            });

            setPreview(
                data.profile_photo || null
            );

        } catch (error) {

            console.error(error);
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
            checked,
            files
        } = e.target;

        if (type === "file") {

            setFormData({

                ...formData,

                [name]:
                    files[0]
            });

            setPreview(

                URL.createObjectURL(
                    files[0]
                )
            );

            return;
        }

        setFormData({

            ...formData,

            [name]:

                type === "checkbox"

                    ? checked

                    : value,
        });
    };


    // =====================================
    // HANDLE SUBMIT
    // =====================================

    const handleSubmit =
        async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            // =====================================
            // FORM DATA
            // =====================================

            const payload =
                new FormData();


            Object.keys(formData)
                .forEach((key) => {

                if (

                    formData[key] !== null &&

                    formData[key] !== ""
                ) {

                    payload.append(

                        key,

                        formData[key]
                    );
                }
            });


            // =====================================
            // UPDATE USER
            // =====================================

            if (userId) {

                await userService.updateUser(

                    userId,

                    payload
                );
            }

            // =====================================
            // CREATE USER
            // =====================================

            else {

                await userService.createUser(
                    payload
                );
            }


            // =====================================
            // SUCCESS
            // =====================================

            alert(
                "User saved successfully"
            );


            navigate(
                "/dashboard/users"
            );

        }

        catch (error) {

            // =====================================
            // FULL ERROR
            // =====================================

            console.error(

                "FULL ERROR:",

                error
            );


            // =====================================
            // RESPONSE
            // =====================================

            console.log(

                "RESPONSE:",

                error.response
            );


            // =====================================
            // VALIDATION DATA
            // =====================================

            console.log(

                "DATA:",

                error.response?.data
            );


            // =====================================
            // ALERT
            // =====================================

            alert(

                JSON.stringify(

                    error.response?.data,

                    null,

                    2
                )
            );
        }

        finally {

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
                max-w-5xl
            "
        >

            <h1
                className="
                    text-3xl
                    font-bold
                    mb-8
                "
            >

                {
                    userId

                        ? "Edit User"

                        : "Add User"
                }

            </h1>


            <form
                onSubmit={handleSubmit}
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

                {/* FIRST NAME */}

                <div>

                    <label className="block mb-2 font-medium">

                        First Name

                    </label>

                    <input
                        type="text"
                        name="first_name"
                        value={formData.first_name}
                        onChange={handleChange}
                        className="w-full border rounded-xl px-4 py-3"
                    />

                </div>


                {/* LAST NAME */}

                <div>

                    <label className="block mb-2 font-medium">

                        Last Name

                    </label>

                    <input
                        type="text"
                        name="last_name"
                        value={formData.last_name}
                        onChange={handleChange}
                        className="w-full border rounded-xl px-4 py-3"
                    />

                </div>


                {/* EMAIL */}

                <div>

                    <label className="block mb-2 font-medium">

                        Email

                    </label>

                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        className="w-full border rounded-xl px-4 py-3"
                        required
                    />

                </div>


                {/* PHONE */}

                <div>

                    <label className="block mb-2 font-medium">

                        Phone

                    </label>

                    <input
                        type="text"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                        className="w-full border rounded-xl px-4 py-3"
                    />

                </div>


                {/* DESIGNATION */}

                <div>

                    <label className="block mb-2 font-medium">

                        Designation

                    </label>

                    <input
                        type="text"
                        name="designation"
                        value={formData.designation}
                        onChange={handleChange}
                        className="w-full border rounded-xl px-4 py-3"
                    />

                </div>


                {/* PASSWORD */}

                <div>

                    <label className="block mb-2 font-medium">

                        Password

                    </label>

                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        className="w-full border rounded-xl px-4 py-3"
                        required={!userId}
                    />

                </div>


                {/* PROFILE PHOTO */}

                <div
                    className="
                        md:col-span-2
                    "
                >

                    <label className="block mb-2 font-medium">

                        Profile Photo

                    </label>

                    <input
                        type="file"
                        name="profile_photo"
                        accept="image/*"
                        onChange={handleChange}
                        className="w-full border rounded-xl px-4 py-3"
                    />


                    {
                        preview && (

                            <img
                                src={preview}
                                alt="Preview"
                                className="
                                    mt-4
                                    w-32
                                    h-32
                                    object-cover
                                    rounded-xl
                                    border
                                "
                            />
                        )
                    }

                </div>


                {/* BUTTON */}

                <div
                    className="
                        md:col-span-2
                    "
                >

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
                        "
                    >

                        {
                            loading

                                ? "Saving..."

                                : userId

                                    ? "Update User"

                                    : "Create User"
                        }

                    </button>

                </div>

            </form>

        </div>
    );
};


export default UserForm;