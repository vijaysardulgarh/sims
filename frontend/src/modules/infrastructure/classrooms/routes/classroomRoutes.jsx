// classroomRoutes.jsx

import { Route } from "react-router-dom";

import ClassroomsList from "../pages/ClassroomsList";
import AddClassroom from "../pages/AddClassroom";
import EditClassroom from "../pages/EditClassroom";

const classroomRoutes = (

    <Route path="classrooms">

        <Route
            index
            element={<ClassroomsList />}
        />

        <Route
            path="add"
            element={<AddClassroom />}
        />

        <Route
            path=":id/edit"
            element={<EditClassroom />}
        />

    </Route>

);

export default classroomRoutes;