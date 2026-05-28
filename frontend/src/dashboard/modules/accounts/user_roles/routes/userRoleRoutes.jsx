import { Route } from "react-router-dom";

import UserRolesListPage from "../pages/UserRolesListPage";
import AddUserRolePage from "../pages/AddUserRolePage";
import EditUserRolePage from "../pages/EditUserRolePage";

const userRoleRoutes = (

    <Route path="user-roles">

        <Route
            index
            element={<UserRolesListPage />}
        />

        <Route
            path="add"
            element={<AddUserRolePage />}
        />

        <Route
            path="edit/:id"
            element={<EditUserRolePage />}
        />

    </Route>
);

export default userRoleRoutes;