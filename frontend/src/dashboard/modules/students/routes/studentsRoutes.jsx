import { Route } from "react-router-dom";

import StudentsList from "../pages/StudentsList";
import AddStudent from "../pages/AddStudent";
import EditStudent from "../pages/EditStudent";
import StudentProfile from "../pages/StudentProfile";

const studentsRoutes = (
  <Route path="students">

    <Route
      path=""
      element={<StudentsList />}
    />

    <Route
      path="add"
      element={<AddStudent />}
    />

    <Route
      path="edit/:id"
      element={<EditStudent />}
    />

    <Route
      path="profile/:id"
      element={<StudentProfile />}
    />

  </Route>
);

export default studentsRoutes;