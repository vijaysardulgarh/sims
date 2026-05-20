import {
    Navigate
} from "react-router-dom";

import {
    useAuth
} from "../dashboard/auth/context/AuthContext";


const ProtectedRoute = ({
    children
}) => {

    const {

        accessToken,

        loading

    } = useAuth();


    // =====================================
    // WAIT FOR AUTH INITIALIZATION
    // =====================================

    if (loading) {

        return (

            <div
                className="
                    flex
                    items-center
                    justify-center
                    h-screen
                    text-xl
                "
            >

                Loading...

            </div>
        );
    }


    // =====================================
    // CHECK TOKEN
    // =====================================

    const token =

        accessToken ||

        localStorage.getItem(
            "access"
        );


    // =====================================
    // NO TOKEN
    // =====================================

    if (!token) {

        return (

            <Navigate
                to="/login"
                replace
            />
        );
    }


    // =====================================
    // AUTHORIZED
    // =====================================

    return children;
};


export default ProtectedRoute;