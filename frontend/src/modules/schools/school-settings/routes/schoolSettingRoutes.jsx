import { Route } from "react-router-dom";

import SchoolSettingsListPage from "../pages/SchoolSettingsListPage";
import AddSchoolSettingPage from "../pages/AddSchoolSettingPage";
import EditSchoolSettingPage from "../pages/EditSchoolSettingPage";

const schoolSettingRoutes = (

    <Route path="school-settings">

        <Route
            index
            element={
                <SchoolSettingsListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddSchoolSettingPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditSchoolSettingPage />
            }
        />

    </Route>
);

export default schoolSettingRoutes;