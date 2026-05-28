import { Route } from "react-router-dom";

import ClassroomsList from "../pages/ClassroomsList";
import AddClassroom from "../pages/AddClassroom";
import EditClassroom from "../pages/EditClassroom";

const classroomRoutes = (
  <>
    <Route
      path="academics/classrooms"
      element={<ClassroomsList />}
    />

    <Route
      path="academics/classrooms/add"
      element={<AddClassroom />}
    />

    <Route
      path="academics/classrooms/edit/:id"
      element={<EditClassroom />}
    />
  </>
);

export default classroomRoutes;