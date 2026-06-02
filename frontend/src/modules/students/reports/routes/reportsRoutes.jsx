import { Route } from "react-router-dom";

import studentStrengthRoutes
from "../student-strength/routes/studentStrengthRoutes";

const reportsRoutes = (

  <Route path="reports">

    {studentStrengthRoutes}

  </Route>

);

export default reportsRoutes;