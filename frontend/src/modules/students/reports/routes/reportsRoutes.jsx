import { Route } from "react-router-dom";

import studentStrengthRoutes
from "../student-strength/routes/studentStrengthRoutes";

import rollCallRoutes
from "../roll-call/routes/rollCallRoutes";

const reportsRoutes = (

    <Route path="reports">

        {studentStrengthRoutes}

        {rollCallRoutes}

    </Route>

);

export default reportsRoutes;