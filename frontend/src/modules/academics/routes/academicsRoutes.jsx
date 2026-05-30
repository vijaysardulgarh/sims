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

// import classSubjectRoutes from
// "../../timetables/class-subjects/routes/classSubjectRoutes";

// import dayRoutes from
// "../../timetables/days/routes/dayRoutes";

// import timetableSlotRoutes from
// "../../timetables/timetable-slots/routes/timetableSlotRoutes";

// import timetableRoutes from
// "../../timetables/timetable/routes/timetableRoutes";

// import classroomRoutes from
// "../../infrastructure/classrooms/routes/classroomRoutes";

import mediumRoutes from
"../mediums/routes/mediumRoutes";

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

    {/* {classSubjectRoutes}

    {dayRoutes}

    {timetableSlotRoutes}

    {timetableRoutes}

    {classroomRoutes} */}

    {mediumRoutes}

    {reportRoutes}
  </>
);

export default academicsRoutes;