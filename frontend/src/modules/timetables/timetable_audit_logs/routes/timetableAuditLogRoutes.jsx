import {
    Route,
} from "react-router-dom";

import TimetableAuditLogListPage
    from "../pages/TimetableAuditLogListPage";

const timetableAuditLogRoutes = (

    <Route path="timetable-audit-logs">

        <Route
            index
            element={
                <TimetableAuditLogListPage />
            }
        />

    </Route>

);

export default timetableAuditLogRoutes;