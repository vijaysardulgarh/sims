import { Route } from "react-router-dom";

import StaffReport from "../StaffReport";

import AttendanceReport from "../AttendanceReport";

import VacancyReport from "../VacancyReport";

import WorkloadReport from "../WorkloadReport";


const reportRoutes = (

    <Route path="reports">

        <Route
            path="staff"
            element={<StaffReport />}
        />

        <Route
            path="attendance"
            element={<AttendanceReport />}
        />

        <Route
            path="vacancy"
            element={<VacancyReport />}
        />

        <Route
            path="workload"
            element={<WorkloadReport />}
        />

    </Route>

);

export default reportRoutes;