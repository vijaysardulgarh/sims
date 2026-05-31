import { Route } from "react-router-dom";

import PrincipalsListPage from "../pages/PrincipalsListPage";

import AddPrincipalPage from "../pages/AddPrincipalPage";

import EditPrincipalPage from "../pages/EditPrincipalPage";

const principalRoutes = (

    <Route path="principals">

        <Route
            index
            element={<PrincipalsListPage />}
        />

        <Route
            path="add"
            element={<AddPrincipalPage />}
        />

        <Route
            path="edit/:id"
            element={<EditPrincipalPage />}
        />

    </Route>
);

export default principalRoutes;