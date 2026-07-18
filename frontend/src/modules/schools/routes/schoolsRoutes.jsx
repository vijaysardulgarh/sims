import { Route } from "react-router-dom";

import schoolRoutes from "../schools/routes/schoolRoutes";
import aboutSchoolRoutes from "../about-schools/routes/aboutSchoolRoutes";
import principalRoutes from "../principals/routes/principalRoutes";

const schoolsRoutes = (
    <Route path="schools">

        {schoolRoutes}

        {aboutSchoolRoutes}

        {principalRoutes}

    </Route>
);

export default schoolsRoutes;