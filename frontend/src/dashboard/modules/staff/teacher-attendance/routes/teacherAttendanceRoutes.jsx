import { Route } from "react-router-dom";

import TeacherAttendanceList from "../pages/TeacherAttendanceList";

import AddTeacherAttendance from "../pages/AddTeacherAttendance";

import EditTeacherAttendance from "../pages/EditTeacherAttendance";


const teacherAttendanceRoutes = (

    <Route path="teacher-attendance">

        <Route
            index
            element={<TeacherAttendanceList />}
        />

        <Route
            path="add"
            element={<AddTeacherAttendance />}
        />

        <Route
            path="edit/:id"
            element={<EditTeacherAttendance />}
        />

    </Route>

);

export default teacherAttendanceRoutes;