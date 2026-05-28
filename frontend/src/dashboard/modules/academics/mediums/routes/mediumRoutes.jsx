import { Route } from "react-router-dom";

import MediumsList from "../pages/MediumsList";
import AddMedium from "../pages/AddMedium";
import EditMedium from "../pages/EditMedium";

const mediumRoutes = (
  <>
    <Route
      path="academics/mediums"
      element={<MediumsList />}
    />

    <Route
      path="academics/mediums/add"
      element={<AddMedium />}
    />

    <Route
      path="academics/mediums/edit/:id"
      element={<EditMedium />}
    />
  </>
);

export default mediumRoutes;