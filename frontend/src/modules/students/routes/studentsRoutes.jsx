import { Route } from "react-router-dom";

import studentListRoutes from
  "../studentsList/routes/studentListRoutes";

import reportsRoutes from
  "../reports/routes/reportsRoutes";

const studentsRoutes = (

  <Route path="students">

    {studentListRoutes}

    {reportsRoutes}

  </Route>

);

export default studentsRoutes;