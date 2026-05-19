import {
    Navigate
} from "react-router-dom";

import {
    useAuth
} from "../../auth/context/AuthContext";


const RoleBasedRoute = ({

    children,

    allowedRoles = [],

}) => {

    const {
        user
    } = useAuth();

    const userRoles =
        user?.roles || [];

    const hasAccess =
        allowedRoles.some(

            role =>
                userRoles.includes(role)
        );

    if (!hasAccess) {

        return (
            <Navigate
                to="/unauthorized"
                replace
            />
        );
    }

    return children;
};

export default RoleBasedRoute;