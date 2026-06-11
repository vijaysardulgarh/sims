import { Route }
from "react-router-dom";


// =====================================
// DASHBOARD HOME
// =====================================

import DashboardHomePage from "./home/pages/DashboardHomePage";


// =====================================
// MODULE ROUTES
// =====================================
import complianceRoutes from "./compliance/routes/complianceRoutes";
import academicsRoutes from "./academics/routes/academicsRoutes";
import accountsRoutes from "./accounts/routes/accountsRoutes";
//import attendanceRoutes from "./accounts/routes/attendanceRoutes";
import communicationRoutes from "./communication/routes/communicationRoutes";
//import examinationRoutes from "./examinations/routes/examinationRoutes";
// import feesRoutes from "./fees/routes/feesRoutes";
// import hostelRoutes from "./hostel/routes/hostelRoutes";
// import libraryRoutes from "./library/routes/libraryRoutes";
import staffRoutes from "./staff/routes/staffRoutes";
import studentsRoutes from "./students/routes/studentsRoutes";
import timetablesRoutes from "./timetables/routes/timetablesRoutes";
// import transportRoutes from "./transport/routes/transportRoutes";
import schoolsRoutes from "./schools/routes/schoolsRoutes.jsx";
import clusterRoutes from "./cluster/routes/clusterRoutes";
import associationModuleRoutes from "./associations/routes/associationModuleRoutes";
import infrastructureRoutes from "./infrastructure/routes/infrastructureRoutes.jsx";

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

    {academicsRoutes}
    {accountsRoutes}
    {communicationRoutes}
{/*     {attendanceRoutes}
    
    {examinationRoutes}
    {feesRoutes}
    {hostelRoutes}
    {libraryRoutes} */}
    {staffRoutes}
    {studentsRoutes}
    {timetablesRoutes}
    {/* {transportRoutes} */}
    {schoolsRoutes}
    {infrastructureRoutes}
    {clusterRoutes}
    {associationModuleRoutes}
    {complianceRoutes}

  </>
);

export default moduleRoutes;