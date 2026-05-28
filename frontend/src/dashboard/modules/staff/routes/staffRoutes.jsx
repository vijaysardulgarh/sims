import { Route } from "react-router-dom";

// import dashboardRoutes from
// "../dashboard/routes/dashboardRoutes";

import staffProfileRoutes from "../profiles/routes/staffProfileRoutes";

import postTypeRoutes from
"../post-types/routes/postTypeRoutes";

import classInchargeRoutes from
"../class-incharge/routes/classInchargeRoutes";

import sanctionedPostRoutes from
"../sanctioned-posts/routes/sanctionedPostRoutes";

import teacherAttendanceRoutes from
"../teacher-attendance/routes/teacherAttendanceRoutes";

// import teacherTimetableRoutes from
// "../teacher-timetable/routes/teacherTimetableRoutes";

// import reportRoutes from
// "../reports/routes/reportRoutes";


const staffRoutes = (

    <Route path="staff">

        {/* {dashboardRoutes} */}

        {staffProfileRoutes}

        {postTypeRoutes}

        {classInchargeRoutes}

        {sanctionedPostRoutes}

        {teacherAttendanceRoutes}

        {/* {teacherTimetableRoutes} */}

        {/* {reportRoutes} */}

    </Route>

);

export default staffRoutes;