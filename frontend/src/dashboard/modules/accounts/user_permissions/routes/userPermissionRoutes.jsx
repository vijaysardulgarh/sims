import { Route } from "react-router-dom";

import UserPermissionsPage from "../pages/UserPermissionsPage";

const userPermissionRoutes = (

    <Route
        path="user-permissions"
        element={<UserPermissionsPage />}
    />

);

export default userPermissionRoutes;