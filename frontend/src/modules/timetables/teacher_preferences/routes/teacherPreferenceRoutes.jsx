import {
    Route,
} from "react-router-dom";

import TeacherPreferenceListPage
    from "../pages/TeacherPreferenceListPage";

import TeacherPreferenceCreatePage
    from "../pages/TeacherPreferenceCreatePage";

import TeacherPreferenceEditPage
    from "../pages/TeacherPreferenceEditPage";

const teacherPreferenceRoutes = (

    <Route path="teacher-preferences">

        <Route
            index
            element={
                <TeacherPreferenceListPage />
            }
        />

        <Route
            path="add"
            element={
                <TeacherPreferenceCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TeacherPreferenceEditPage />
            }
        />

    </Route>

);

export default teacherPreferenceRoutes;