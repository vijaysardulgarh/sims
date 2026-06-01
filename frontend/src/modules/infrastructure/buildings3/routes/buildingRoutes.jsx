// src/modules/infrastructure/buildings/routes/buildingRoutes.jsx

import { Route } from "react-router-dom";

import BuildingsListPage
    from "../pages/BuildingsListPage";

import BuildingFormPage
    from "../pages/BuildingFormPage";

const buildingRoutes = (

    <Route path="buildings">

        <Route
            index
            element={
                <BuildingsListPage />
            }
        />

        <Route
            path="add"
            element={
                <BuildingFormPage />
            }
        />

        <Route
            path=":id/edit"
            element={
                <BuildingFormPage />
            }
        />

    </Route>

);

export default buildingRoutes;