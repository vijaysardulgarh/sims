import { Route } from "react-router-dom";

import PermissionsListPage from "../pages/PermissionsListPage";
import AddPermissionPage from "../pages/AddPermissionPage";
import EditPermissionPage from "../pages/EditPermissionPage";

const permissionRoutes = (

    <Route path="permissions">

        <Route
            index
            element={<PermissionsListPage />}
        />

        <Route
            path="add"
            element={<AddPermissionPage />}
        />

        <Route
            path="edit/:id"
            element={<EditPermissionPage />}
        />

    </Route>
);

export default permissionRoutes;