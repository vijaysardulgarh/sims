import {
    Route,
} from "react-router-dom";

import TimetableEntryListPage
    from "../pages/TimetableEntryListPage";

import TimetableEntryCreatePage
    from "../pages/TimetableEntryCreatePage";

import TimetableEntryEditPage
    from "../pages/TimetableEntryEditPage";

const timetableEntryRoutes = (

    <Route path="timetable-entries">

        <Route
            index
            element={
                <TimetableEntryListPage />
            }
        />

        <Route
            path="add"
            element={
                <TimetableEntryCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TimetableEntryEditPage />
            }
        />

    </Route>

);

export default timetableEntryRoutes;