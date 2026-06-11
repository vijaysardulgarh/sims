import {
    Route,
} from "react-router-dom";

import TeacherAvailabilityListPage
    from "../pages/TeacherAvailabilityListPage";

import TeacherAvailabilityCreatePage
    from "../pages/TeacherAvailabilityCreatePage";

import TeacherAvailabilityEditPage
    from "../pages/TeacherAvailabilityEditPage";

const teacherAvailabilityRoutes = (

    <Route path="teacher-availabilities">

        <Route
            index
            element={
                <TeacherAvailabilityListPage />
            }
        />

        <Route
            path="add"
            element={
                <TeacherAvailabilityCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <TeacherAvailabilityEditPage />
            }
        />

    </Route>

);

export default teacherAvailabilityRoutes;