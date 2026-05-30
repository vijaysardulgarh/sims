import { Route } from "react-router-dom";

import ModulesListPage from "../pages/ModulesListPage";

import AddModulePage from "../pages/AddModulePage";

import EditModulePage from "../pages/EditModulePage";


const systemModulesRoutes = (

    <Route path="system-modules">

        <Route
            index
            element={<ModulesListPage />}
        />

        <Route
            path="add"
            element={<AddModulePage />}
        />

        <Route
            path="edit/:id"
            element={<EditModulePage />}
        />

    </Route>

);

export default systemModulesRoutes;