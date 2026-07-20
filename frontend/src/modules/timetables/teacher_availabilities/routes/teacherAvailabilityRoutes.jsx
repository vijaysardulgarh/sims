import { Route } from "react-router-dom";

import TeacherAvailabilityListPage
    from "../pages/TeacherAvailabilityListPage";

const teacherAvailabilityRoutes = (

    <Route path="teacher-availabilities">

        <Route
            index
            element={
                <TeacherAvailabilityListPage />
            }
        />

    </Route>

);

export default teacherAvailabilityRoutes;