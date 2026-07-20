import {
    Route,
} from "react-router-dom";

import TeacherPreferenceListPage
    from "../pages/TeacherPreferenceListPage";

const teacherPreferenceRoutes = (

    <Route path="teacher-preferences">

        <Route
            index
            element={
                <TeacherPreferenceListPage />
            }
        />

    </Route>

);

export default teacherPreferenceRoutes;