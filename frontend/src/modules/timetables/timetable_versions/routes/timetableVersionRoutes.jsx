import {
    Route,
} from "react-router-dom";

import TimetableVersionListPage
    from "../pages/TimetableVersionListPage";

import TimetableVersionCreatePage
    from "../pages/TimetableVersionCreatePage";

import TimetableVersionEditPage
    from "../pages/TimetableVersionEditPage";

const timetableVersionRoutes = (

    <Route path="timetable-versions">

        <Route
            index
            element={
                <TimetableVersionListPage />
            }
        />

        <Route
            path="add"
            element={
                <TimetableVersionCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TimetableVersionEditPage />
            }
        />

    </Route>

);

export default timetableVersionRoutes;