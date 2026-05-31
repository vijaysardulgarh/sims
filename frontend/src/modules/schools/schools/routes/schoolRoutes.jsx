import { Route } from "react-router-dom";

import SchoolListPage from "../pages/SchoolListPage";
import AddSchoolPage from "../pages/AddSchoolPage";
import EditSchoolPage from "../pages/EditSchoolPage";

const schoolRoutes = (
    <Route path="schools">
        <Route index element={<SchoolListPage />} />
        <Route path="add" element={<AddSchoolPage />} />
        <Route path="edit/:id" element={<EditSchoolPage />} />
    </Route>
);

export default schoolRoutes;