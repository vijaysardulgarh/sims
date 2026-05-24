import { Route }
from "react-router-dom";


// =====================================
// DASHBOARD HOME
// =====================================

import DashboardHomePage from "../home/pages/DashboardHomePage";


// =====================================
// MODULE ROUTES
// =====================================

import studentsRoutes from "./students/routes/studentsRoutes";

import accountsRoutes from "./accounts/routes/accountsRoutes";


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

    {accountsRoutes}

  </>
);

export default moduleRoutes;