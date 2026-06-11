import {
    Route,
} from "react-router-dom";

import TeacherWorkloadListPage
    from "../pages/TeacherWorkloadListPage";

import TeacherWorkloadCreatePage
    from "../pages/TeacherWorkloadCreatePage";

import TeacherWorkloadEditPage
    from "../pages/TeacherWorkloadEditPage";

const teacherWorkloadRoutes = (

    <Route path="teacher-workloads">

        <Route
            index
            element={
                <TeacherWorkloadListPage />
            }
        />

        <Route
            path="add"
            element={
                <TeacherWorkloadCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TeacherWorkloadEditPage />
            }
        />

    </Route>

);

export default teacherWorkloadRoutes;