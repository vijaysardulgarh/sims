// src/modules/schools/routes/schoolRoutes.jsx

import { Route } from "react-router-dom";

import SchoolsListPage from "../pages/SchoolsListPage";
import SchoolCreatePage from "../pages/SchoolCreatePage";
import SchoolEditPage from "../pages/SchoolEditPage";
import SchoolViewPage from "../pages/SchoolViewPage";

const schoolRoutes = (

    <Route path="schools">

        <Route
            index
            element={<SchoolsListPage />}
        />

        <Route
            path="create"
            element={<SchoolCreatePage />}
        />

        <Route
            path=":id"
            element={<SchoolViewPage />}
        />

        <Route
            path=":id/edit"
            element={<SchoolEditPage />}
        />

    </Route>
);

export default schoolRoutes;