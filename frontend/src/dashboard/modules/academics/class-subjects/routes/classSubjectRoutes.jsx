import { Route } from "react-router-dom";

import ClassSubjectsList from "../pages/ClassSubjectsList";
import AddClassSubject from "../pages/AddClassSubject";
import EditClassSubject from "../pages/EditClassSubject";

const classSubjectRoutes = (
  <>
    <Route
      path="academics/class-subjects"
      element={<ClassSubjectsList />}
    />

    <Route
      path="academics/class-subjects/add"
      element={<AddClassSubject />}
    />

    <Route
      path="academics/class-subjects/edit/:id"
      element={<EditClassSubject />}
    />
  </>
);

export default classSubjectRoutes;