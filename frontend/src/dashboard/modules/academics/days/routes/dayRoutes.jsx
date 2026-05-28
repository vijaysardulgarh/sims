import { Route } from "react-router-dom";

import DaysList from "../pages/DaysList";
import AddDay from "../pages/AddDay";
import EditDay from "../pages/EditDay";

const dayRoutes = (
  <>
    <Route
      path="academics/days"
      element={<DaysList />}
    />

    <Route
      path="academics/days/add"
      element={<AddDay />}
    />

    <Route
      path="academics/days/edit/:id"
      element={<EditDay />}
    />
  </>
);

export default dayRoutes;