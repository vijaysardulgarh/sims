import {
    Route,
} from "react-router-dom";

import SubstituteAssignmentListPage
    from "../pages/SubstituteAssignmentListPage";

import SubstituteAssignmentCreatePage
    from "../pages/SubstituteAssignmentCreatePage";

import SubstituteAssignmentEditPage
    from "../pages/SubstituteAssignmentEditPage";

const substituteAssignmentRoutes = (

    <Route path="substitute-assignments">

        <Route
            index
            element={
                <SubstituteAssignmentListPage />
            }
        />

        <Route
            path="add"
            element={
                <SubstituteAssignmentCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <SubstituteAssignmentEditPage />
            }
        />

    </Route>

);

export default substituteAssignmentRoutes;