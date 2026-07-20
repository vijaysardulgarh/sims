import { Route } from "react-router-dom";

import WorkingDaysPage from "../pages/WorkingDaysPage";

const workingDayRoutes = (

    <Route path="working-days">

        <Route
            index
            element={<WorkingDaysPage />}
        />

    </Route>

);

export default workingDayRoutes;