import { Route } from "react-router-dom";


// =========================================
// DASHBOARD
// =========================================

import AcademicDashboard from
"../dashboard/AcademicDashboard";


// =========================================
// SUBMODULE ROUTES
// =========================================

import classRoutes from
"../classes/routes/classRoutes";

import streamRoutes from
"../streams/routes/streamRoutes";

import sectionRoutes from
"../sections/routes/sectionRoutes";

import subjectRoutes from
"../subjects/routes/subjectRoutes";


import mediumRoutes from
"../mediums/routes/mediumRoutes";

import academicSessionRoutes from
"../sessions/routes/academicSessionRoutes";

import reportRoutes from
"../reports/routes/reportRoutes";


// =========================================
// ACADEMICS ROUTES
// =========================================

const academicsRoutes = (
  <>
    {/* ===================================== */}
    {/* DASHBOARD */}
    {/* ===================================== */}

    <Route
      path="academics"
      element={<AcademicDashboard />}
    />

    {/* ===================================== */}
    {/* SUBMODULE ROUTES */}
    {/* ===================================== */}

    {classRoutes}

    {streamRoutes}

    {sectionRoutes}

    {subjectRoutes}

    {mediumRoutes}

    {academicSessionRoutes}

    {reportRoutes}
  </>
);

export default academicsRoutes;