import {
    Route,
} from "react-router-dom";

import BellScheduleListPage
    from "../pages/BellScheduleListPage";

import BellScheduleCreatePage
    from "../pages/BellScheduleCreatePage";

import BellScheduleEditPage
    from "../pages/BellScheduleEditPage";

const bellScheduleRoutes = (

    <Route path="bell-schedules">

        <Route
            index
            element={<BellScheduleListPage />}
        />

        <Route
            path="add"
            element={<BellScheduleCreatePage />}
        />

        <Route
            path="edit/:id"
            element={<BellScheduleEditPage />}
        />

    </Route>

);

export default bellScheduleRoutes;