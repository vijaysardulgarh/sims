import {
    Route,
} from "react-router-dom";

import TimetableConflictListPage
    from "../pages/TimetableConflictListPage";

import TimetableConflictCreatePage
    from "../pages/TimetableConflictCreatePage";

import TimetableConflictEditPage
    from "../pages/TimetableConflictEditPage";

const timetableConflictRoutes = (

    <Route path="timetable-conflicts">

        <Route
            index
            element={
                <TimetableConflictListPage />
            }
        />

        <Route
            path="add"
            element={
                <TimetableConflictCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TimetableConflictEditPage />
            }
        />

    </Route>

);

export default timetableConflictRoutes;