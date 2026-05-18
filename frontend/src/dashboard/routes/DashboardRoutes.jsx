import { Routes, Route } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

import roleRoutes from "../roles/roleRoutes";
import moduleRoutes from "../modules/moduleRoutes";

const DashboardRoutes = () => {
  return (
    <Routes>

      <Route
        path="/dashboard"
        element={<DashboardLayout />}
      >

        {roleRoutes}

        {moduleRoutes}

      </Route>

    </Routes>
  );
};

export default DashboardRoutes;