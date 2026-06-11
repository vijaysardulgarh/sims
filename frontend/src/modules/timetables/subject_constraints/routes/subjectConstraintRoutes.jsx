import {
    Route,
} from "react-router-dom";

import SubjectConstraintListPage
    from "../pages/SubjectConstraintListPage";

import SubjectConstraintCreatePage
    from "../pages/SubjectConstraintCreatePage";

import SubjectConstraintEditPage
    from "../pages/SubjectConstraintEditPage";

const subjectConstraintRoutes = (

    <Route path="subject-constraints">

        <Route
            index
            element={
                <SubjectConstraintListPage />
            }
        />

        <Route
            path="add"
            element={
                <SubjectConstraintCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <SubjectConstraintEditPage />
            }
        />

    </Route>

);

export default subjectConstraintRoutes;