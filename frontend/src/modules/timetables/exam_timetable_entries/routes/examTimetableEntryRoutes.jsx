import {
    Route,
} from "react-router-dom";

import ExamTimetableEntryListPage
    from "../pages/ExamTimetableEntryListPage";

import ExamTimetableEntryCreatePage
    from "../pages/ExamTimetableEntryCreatePage";

import ExamTimetableEntryEditPage
    from "../pages/ExamTimetableEntryEditPage";

const examTimetableEntryRoutes = (

    <Route path="exam-timetable-entries">

        <Route
            index
            element={
                <ExamTimetableEntryListPage />
            }
        />

        <Route
            path="add"
            element={
                <ExamTimetableEntryCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <ExamTimetableEntryEditPage />
            }
        />

    </Route>

);

export default examTimetableEntryRoutes;