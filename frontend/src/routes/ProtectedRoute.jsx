import {
    Navigate
} from "react-router-dom";

import {
    useAuth
} from "../auth/context/AuthContext";


const ProtectedRoute = ({
    children
}) => {

    const {
        accessToken
    } = useAuth();

    if (!accessToken) {

        return (
            <Navigate
                to="/login"
            />
        );
    }

    return children;
};

export default ProtectedRoute;