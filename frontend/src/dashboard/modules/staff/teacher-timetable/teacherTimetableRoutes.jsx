import { Route } from "react-router-dom";

import TeacherTimetable from "../TeacherTimetable";

import TeacherWorkload from "../TeacherWorkload";

import TeacherFreePeriods from "../TeacherFreePeriods";


const teacherTimetableRoutes = (

    <>

        <Route
            path="teacher-timetable/:staffId"
            element={<TeacherTimetable />}
        />

        <Route
            path="teacher-workload/:staffId"
            element={<TeacherWorkload />}
        />

        <Route
            path="teacher-free-periods/:staffId"
            element={<TeacherFreePeriods />}
        />

    </>

);

export default teacherTimetableRoutes;