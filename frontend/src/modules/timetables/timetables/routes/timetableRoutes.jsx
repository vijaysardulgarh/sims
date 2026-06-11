import {
    Route,
} from "react-router-dom";

import TimetableListPage
    from "../pages/TimetableListPage";

import TimetableCreatePage
    from "../pages/TimetableCreatePage";

import TimetableEditPage
    from "../pages/TimetableEditPage";

const timetableRoutes = (

    <Route path="timetables">

        <Route
            index
            element={
                <TimetableListPage />
            }
        />

        <Route
            path="add"
            element={
                <TimetableCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TimetableEditPage />
            }
        />

    </Route>

);

export default timetableRoutes;