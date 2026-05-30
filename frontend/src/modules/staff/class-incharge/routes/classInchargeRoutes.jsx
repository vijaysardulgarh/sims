import { Route } from "react-router-dom";

import ClassInchargeList from "../pages/ClassInchargeList";

import AddClassIncharge from "../pages/AddClassIncharge";

import EditClassIncharge from "../pages/EditClassIncharge";


const classInchargeRoutes = (

    <Route path="class-incharge">

        <Route
            index
            element={<ClassInchargeList />}
        />

        <Route
            path="add"
            element={<AddClassIncharge />}
        />

        <Route
            path="edit/:id"
            element={<EditClassIncharge />}
        />

    </Route>

);

export default classInchargeRoutes;