import {
    Route,
} from "react-router-dom";

import TeacherWorkloadListPage
    from "../pages/TeacherWorkloadListPage";

const teacherWorkloadRoutes = (

    <Route path="teacher-workloads">

        <Route
            index
            element={
                <TeacherWorkloadListPage />
            }
        />

    </Route>

);

export default teacherWorkloadRoutes;