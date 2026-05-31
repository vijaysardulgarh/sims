import { Route } from "react-router-dom";
import { Outlet } from "react-router-dom";

import classroomRoutes from "../classrooms/routes/classroomRoutes";

const infrastructureRoutes = (

    <Route
        path="infrastructure"
        element={<Outlet />}
    >

        {classroomRoutes}

    </Route>

);

export default infrastructureRoutes;