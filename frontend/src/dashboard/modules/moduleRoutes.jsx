import { Route }
from "react-router-dom";


// =====================================
// DASHBOARD HOME
// =====================================

import DashboardHomePage from "./home/pages/DashboardHomePage";


// =====================================
// MODULE ROUTES
// =====================================

import academicsRoutes from "./academics/routes/academicsRoutes";
import accountsRoutes from "./accounts/routes/accountsRoutes";
//import attendanceRoutes from "./accounts/routes/attendanceRoutes";
//import communicationRoutes from "./communication/routes/communicationRoutes";
//import examinationRoutes from "./examinations/routes/examinationRoutes";
// import feesRoutes from "./fees/routes/feesRoutes";
// import hostelRoutes from "./hostel/routes/hostelRoutes";
// import libraryRoutes from "./library/routes/libraryRoutes";
import staffRoutes from "./staff/routes/staffRoutes";
import studentsRoutes from "./students/routes/studentsRoutes";
// import timetableRoutes from "./timetable/routes/timetableRoutes";
// import transportRoutes from "./transport/routes/transportRoutes";
import schoolRoutes from "./schools/routes/schoolRoutes";
import clusterRoutes from "./cluster/routes/clusterRoutes";
import associationModuleRoutes from "./associations/routes/associationModuleRoutes";

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
{/*     {attendanceRoutes}
    {communicationRoutes}
    {examinationRoutes}
    {feesRoutes}
    {hostelRoutes}
    {libraryRoutes} */}
    {staffRoutes}
    {studentsRoutes}
    {/* {timetableRoutes}
    {transportRoutes} */}
    {schoolRoutes}
    
    {clusterRoutes}
    {associationModuleRoutes}

  </>
);

export default moduleRoutes;