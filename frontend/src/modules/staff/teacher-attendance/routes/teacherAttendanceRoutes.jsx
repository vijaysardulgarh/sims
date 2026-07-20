import { Route } from "react-router-dom";

import TeacherAttendancePage from "../pages/TeacherAttendancePage";

const teacherAttendanceRoutes = (
  <Route path="teacher-attendance">
    <Route
      index
      element={<TeacherAttendancePage />}
    />
  </Route>
);

export default teacherAttendanceRoutes;