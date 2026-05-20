import { Route }
from "react-router-dom";


// =====================================
// DASHBOARD HOME
// =====================================

import DashboardHomePage
from "../home/pages/DashboardHomePage";


// =====================================
// MODULE ROUTES
// =====================================

import studentsRoutes
from "./students/routes/studentsRoutes";

import accessControlRoutes
from "./access_control/routes/accessControlRoutes";


// =====================================
// ROUTES
// =====================================

const moduleRoutes = (

  <>

    {/* ================================= */}
    {/* DASHBOARD HOME */}
    {/* ================================= */}

    <Route
      index
      element={<DashboardHomePage />}
    />


    {/* ================================= */}
    {/* MODULES */}
    {/* ================================= */}

    {studentsRoutes}

    {accessControlRoutes}

  </>
);

export default moduleRoutes;