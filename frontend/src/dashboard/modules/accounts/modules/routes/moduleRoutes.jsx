import { Route } from "react-router-dom";

import ModulesListPage from "../pages/ModulesListPage";

import AddModulePage from "../pages/AddModulePage";

import EditModulePage from "../pages/EditModulePage";


const moduleRoutes = (

    <Route path="modules">

        <Route
            index
            element={<ModulesListPage />}
        />

        <Route
            path="add"
            element={<AddModulePage />}
        />

        <Route
            path=":id/edit"
            element={<EditModulePage />}
        />

    </Route>

);

export default moduleRoutes;