import {
    Route,
} from "react-router-dom";

import SubjectRequirementListPage
    from "../pages/SubjectRequirementListPage";

import SubjectRequirementCreatePage
    from "../pages/SubjectRequirementCreatePage";

import SubjectRequirementEditPage
    from "../pages/SubjectRequirementEditPage";

const subjectRequirementRoutes = (

    <Route path="subject-requirements">

        <Route
            index
            element={
                <SubjectRequirementListPage />
            }
        />

        <Route
            path="add"
            element={
                <SubjectRequirementCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <SubjectRequirementEditPage />
            }
        />

    </Route>

);

export default subjectRequirementRoutes;