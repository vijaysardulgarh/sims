import { Route } from "react-router-dom";

import RolesListPage from "../pages/RolesListPage";

import AddRolePage from "../pages/AddRolePage";

import EditRolePage from "../pages/EditRolePage";


const roleRoutes = (

    <Route path="roles">

        <Route
            index
            element={<RolesListPage />}
        />

        <Route
            path="add"
            element={<AddRolePage />}
        />

        <Route
            path="edit/:id"
            element={<EditRolePage />}
        />

    </Route>

);

export default roleRoutes;