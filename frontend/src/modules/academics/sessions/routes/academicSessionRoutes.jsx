import { Route } from "react-router-dom";

import AcademicSessionsListPage from
    "../pages/AcademicSessionsListPage";

import AddAcademicSessionPage from
    "../pages/AddAcademicSessionPage";

import EditAcademicSessionPage from
    "../pages/EditAcademicSessionPage";

const academicSessionRoutes = (
    <>
        <Route
            path="academics/sessions"
            element={
                <AcademicSessionsListPage />
            }
        />

        <Route
            path="academics/sessions/add"
            element={
                <AddAcademicSessionPage />
            }
        />

        <Route
            path="academics/sessions/edit/:id"
            element={
                <EditAcademicSessionPage />
            }
        />
    </>
);

export default academicSessionRoutes;