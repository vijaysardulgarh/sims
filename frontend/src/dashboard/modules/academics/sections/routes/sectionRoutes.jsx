import { Route } from "react-router-dom";

import SectionsList from "../pages/SectionsList";
import AddSection from "../pages/AddSection";
import EditSection from "../pages/EditSection";

const sectionRoutes = (
  <>
    <Route
      path="academics/sections"
      element={<SectionsList />}
    />

    <Route
      path="academics/sections/add"
      element={<AddSection />}
    />

    <Route
      path="academics/sections/edit/:id"
      element={<EditSection />}
    />
  </>
);

export default sectionRoutes;