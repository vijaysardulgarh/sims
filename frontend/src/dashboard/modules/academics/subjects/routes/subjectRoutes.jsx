import { Route } from "react-router-dom";

import SubjectsList from "../pages/SubjectsList";
import AddSubject from "../pages/AddSubject";
import EditSubject from "../pages/EditSubject";

const subjectRoutes = (
  <>
    <Route
      path="academics/subjects"
      element={<SubjectsList />}
    />

    <Route
      path="academics/subjects/add"
      element={<AddSubject />}
    />

    <Route
      path="academics/subjects/edit/:id"
      element={<EditSubject />}
    />
  </>
);

export default subjectRoutes;