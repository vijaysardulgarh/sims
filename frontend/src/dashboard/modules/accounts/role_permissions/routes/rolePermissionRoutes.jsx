import { Route } from "react-router-dom";

import RolePermissionsPage from "../pages/RolePermissionsPage";

const rolePermissionRoutes = (

    <Route
        path="roles/:id/permissions"
        element={<RolePermissionsPage />}
    />

);

export default rolePermissionRoutes;