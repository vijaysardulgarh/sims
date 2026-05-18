import { Route } from "react-router-dom";

import SuperAdminDashboard from "../roles/super-admin/Dashboard";
import AdminDashboard from "../roles/admin/Dashboard";
import TeacherDashboard from "../roles/teacher/Dashboard";

const roleRoutes = (
  <>
    <Route
      path="super-admin"
      element={<SuperAdminDashboard />}
    />

    <Route
      path="admin"
      element={<AdminDashboard />}
    />

    <Route
      path="teacher"
      element={<TeacherDashboard />}
    />
  </>
);

export default roleRoutes;