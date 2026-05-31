import { Route } from "react-router-dom";

import schoolRoutes from "../schools/routes/schoolRoutes";
import aboutSchoolRoutes from "../about-schools/routes/aboutSchoolRoutes";

const schoolsRoutes = (
    <Route path="schools">
        {schoolRoutes}
        {aboutSchoolRoutes}
    </Route>
);

export default schoolsRoutes;