import {
    Route,
} from "react-router-dom";

import TimetableApprovalListPage
    from "../pages/TimetableApprovalListPage";

import TimetableApprovalCreatePage
    from "../pages/TimetableApprovalCreatePage";

import TimetableApprovalEditPage
    from "../pages/TimetableApprovalEditPage";

const timetableApprovalRoutes = (

    <Route path="timetable-approvals">

        <Route
            index
            element={
                <TimetableApprovalListPage />
            }
        />

        <Route
            path="add"
            element={
                <TimetableApprovalCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TimetableApprovalEditPage />
            }
        />

    </Route>

);

export default timetableApprovalRoutes;