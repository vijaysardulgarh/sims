import {
    Route,
} from "react-router-dom";

import PeriodDefinitionListPage
    from "../pages/PeriodDefinitionListPage";

import PeriodDefinitionCreatePage
    from "../pages/PeriodDefinitionCreatePage";

import PeriodDefinitionEditPage
    from "../pages/PeriodDefinitionEditPage";

const periodDefinitionRoutes = (

    <Route path="period-definitions">

        <Route
            index
            element={
                <PeriodDefinitionListPage />
            }
        />

        <Route
            path="add"
            element={
                <PeriodDefinitionCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <PeriodDefinitionEditPage />
            }
        />

    </Route>

);

export default periodDefinitionRoutes;