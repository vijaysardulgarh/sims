import {
    useEffect,
    useState
} from "react";

import {
    useParams,
    Link
} from "react-router-dom";

import userService
from "../../services/userService";


const UserProfilePage = () => {

    const {
        id
    } = useParams();


    const [user,
        setUser] =
        useState(null);

    const [loading,
        setLoading] =
        useState(true);


    useEffect(() => {

        fetchUser();

    }, []);


    const fetchUser =
        async () => {

        try {

            const data =
                await userService.getUser(id);

            setUser(data);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    };


    if (loading) {

        return (

            <div className="p-10 text-xl">

                Loading profile...

            </div>
        );
    }


    if (!user) {

        return (

            <div className="p-10 text-red-600">

                User not found.

            </div>
        );
    }


    return (

        <div className="bg-white rounded-2xl shadow-sm p-6 max-w-3xl">

            <div className="flex items-center justify-between mb-6">

                <h1 className="text-3xl font-bold">

                    User Profile

                </h1>


                <Link
                    to={`/dashboard/users/edit/${user.id}`}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl"
                >

                    Edit User

                </Link>

            </div>


            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                <div>

                    <p className="text-gray-500 mb-1">
                        First Name
                    </p>

                    <h2 className="text-xl font-semibold">
                        {user.first_name}
                    </h2>

                </div>


                <div>

                    <p className="text-gray-500 mb-1">
                        Last Name
                    </p>

                    <h2 className="text-xl font-semibold">
                        {user.last_name}
                    </h2>

                </div>


                <div>

                    <p className="text-gray-500 mb-1">
                        Email
                    </p>

                    <h2 className="text-xl font-semibold">
                        {user.email}
                    </h2>

                </div>


                <div>

                    <p className="text-gray-500 mb-1">
                        Phone
                    </p>

                    <h2 className="text-xl font-semibold">
                        {user.phone}
                    </h2>

                </div>


                <div>

                    <p className="text-gray-500 mb-1">
                        Active
                    </p>

                    <h2 className="text-xl font-semibold">

                        {
                            user.is_active
                                ? "Yes"
                                : "No"
                        }

                    </h2>

                </div>

            </div>

        </div>
    );
};


export default UserProfilePage;