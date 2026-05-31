import { Route } from "react-router-dom";

import AboutSchoolListPage from "../pages/AboutSchoolListPage";

import AddAboutSchoolPage from "../pages/AddAboutSchoolPage";

import EditAboutSchoolPage from "../pages/EditAboutSchoolPage";

const aboutSchoolRoutes = (

    <Route path="about-schools">

        <Route
            index
            element={
                <AboutSchoolListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddAboutSchoolPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditAboutSchoolPage />
            }
        />

    </Route>
);

export default aboutSchoolRoutes;