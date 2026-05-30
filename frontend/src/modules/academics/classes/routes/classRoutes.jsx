import { Route } from "react-router-dom";

import ClassesList from "../pages/ClassesList";
import AddClass from "../pages/AddClass";
import EditClass from "../pages/EditClass";

const classRoutes = (
  <>
    <Route
      path="academics/classes"
      element={<ClassesList />}
    />

    <Route
      path="academics/classes/add"
      element={<AddClass />}
    />

    <Route
      path="academics/classes/edit/:id"
      element={<EditClass />}
    />
  </>
);

export default classRoutes;