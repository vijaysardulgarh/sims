import {
    Route,
} from "react-router-dom";

import WorkingDayListPage
    from "../pages/WorkingDayListPage";

import WorkingDayCreatePage
    from "../pages/WorkingDayCreatePage";

import WorkingDayEditPage
    from "../pages/WorkingDayEditPage";

const workingDayRoutes = (

    <Route path="working-days">

        <Route
            index
            element={
                <WorkingDayListPage />
            }
        />

        <Route
            path="add"
            element={
                <WorkingDayCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <WorkingDayEditPage />
            }
        />

    </Route>

);

export default workingDayRoutes;