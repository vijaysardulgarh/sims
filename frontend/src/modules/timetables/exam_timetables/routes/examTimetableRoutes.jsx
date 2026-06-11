import {
    Route,
} from "react-router-dom";

import ExamTimetableListPage
    from "../pages/ExamTimetableListPage";

import ExamTimetableCreatePage
    from "../pages/ExamTimetableCreatePage";

import ExamTimetableEditPage
    from "../pages/ExamTimetableEditPage";

const examTimetableRoutes = (

    <Route path="exam-timetables">

        <Route
            index
            element={
                <ExamTimetableListPage />
            }
        />

        <Route
            path="add"
            element={
                <ExamTimetableCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <ExamTimetableEditPage />
            }
        />

    </Route>

);

export default examTimetableRoutes;