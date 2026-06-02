import { Route } from "react-router-dom";

import StudentStrengthReport
from "../pages/StudentStrengthReport";

const studentStrengthRoutes = (

  <Route path="student-strength">

    <Route
      index
      element={
        <StudentStrengthReport />
      }
    />

  </Route>

);

export default studentStrengthRoutes;