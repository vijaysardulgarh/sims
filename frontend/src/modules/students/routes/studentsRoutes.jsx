import { Route } from "react-router-dom";

import studentRoutes from
  "../students/routes/studentRoutes";

import reportsRoutes from
  "../reports/routes/reportsRoutes";

const studentsRoutes = (

  <Route path="students">

    {studentRoutes}

    {reportsRoutes}

  </Route>

);

export default studentsRoutes;