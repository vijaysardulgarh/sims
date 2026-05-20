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
    // WAIT FOR AUTH LOAD
    // =====================================

    if (loading) {

        return (

            <div>

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
    // REDIRECT
    // =====================================

    if (!token) {

        return (

            <Navigate
                to="/login"
                replace
            />
        );
    }


    return children;
};


export default ProtectedRoute;