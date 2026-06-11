import {
    Route,
} from "react-router-dom";

import TimetablePublicationListPage
    from "../pages/TimetablePublicationListPage";

import TimetablePublicationCreatePage
    from "../pages/TimetablePublicationCreatePage";

import TimetablePublicationEditPage
    from "../pages/TimetablePublicationEditPage";

const timetablePublicationRoutes = (

    <Route path="timetable-publications">

        <Route
            index
            element={
                <TimetablePublicationListPage />
            }
        />

        <Route
            path="add"
            element={
                <TimetablePublicationCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TimetablePublicationEditPage />
            }
        />

    </Route>

);

export default timetablePublicationRoutes;