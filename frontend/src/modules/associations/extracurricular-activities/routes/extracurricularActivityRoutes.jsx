import { Route } from "react-router-dom";

import ExtracurricularActivityListPage from "../pages/ExtracurricularActivityListPage";
import ExtracurricularActivityAddPage from "../pages/ExtracurricularActivityAddPage";
import ExtracurricularActivityEditPage from "../pages/ExtracurricularActivityEditPage";

const extracurricularActivityRoutes = (

    <>

        <Route
            path="associations/extracurricular-activities"
            element={<ExtracurricularActivityListPage />}
        />

        <Route
            path="associations/extracurricular-activities/add"
            element={<ExtracurricularActivityAddPage />}
        />

        <Route
            path="associations/extracurricular-activities/edit/:id"
            element={<ExtracurricularActivityEditPage />}
        />

    </>

);

export default extracurricularActivityRoutes;