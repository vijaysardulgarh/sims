import {
    Route,
} from "react-router-dom";

import SubjectConstraintListPage
    from "../pages/SubjectConstraintListPage";


const subjectConstraintRoutes = (

    <Route
        path="subject-constraints"
    >

        <Route
            index
            element={
                <SubjectConstraintListPage />
            }
        />

    </Route>

);

export default subjectConstraintRoutes;