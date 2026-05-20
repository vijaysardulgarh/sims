import { Route } from "react-router-dom";


// =====================================
// FORMS
// =====================================

import PermissionsForm
from "../forms/PermissionsForm.jsx";


// =====================================
// ROLE PAGES
// =====================================

import RolesListPage
from "../pages/roles/RolesListPage";

import AddRolePage
from "../pages/roles/AddRolePage";

import EditRolePage
from "../pages/roles/EditRolePage";


// =====================================
// USER PAGES
// =====================================

import UsersListPage
from "../pages/users/UsersListPage";

import AddUserPage
from "../pages/users/AddUserPage";

import EditUserPage
from "../pages/users/EditUserPage";

import UserProfilePage
from "../pages/users/UserProfilePage";


// =====================================
// PERMISSION PAGES
// =====================================

import PermissionsListPage
from "../pages/permissions/PermissionsListPage";

import RolePermissionsPage
from "../pages/permissions/RolePermissionsPage";

import UserRolesPage
from "../pages/permissions/UserRolesPage";


// =====================================
// ROUTES
// =====================================

const accessControlRoutes = (

    <>

        {/* ================================= */}
        {/* ROLES */}
        {/* ================================= */}

        <Route
            path="roles"
            element={<RolesListPage />}
        />

        <Route
            path="roles/add"
            element={<AddRolePage />}
        />

        <Route
            path="roles/edit/:id"
            element={<EditRolePage />}
        />


        {/* ================================= */}
        {/* USERS */}
        {/* ================================= */}

        <Route
            path="users"
            element={<UsersListPage />}
        />

        <Route
            path="users/add"
            element={<AddUserPage />}
        />

        <Route
            path="users/edit/:id"
            element={<EditUserPage />}
        />

        <Route
            path="users/profile/:id"
            element={<UserProfilePage />}
        />


        {/* ================================= */}
        {/* PERMISSIONS */}
        {/* ================================= */}

        <Route
            path="permissions"
            element={<PermissionsListPage />}
        />

        <Route
            path="permissions/add"
            element={<PermissionsForm />}
        />

        <Route
            path="permissions/edit/:id"
            element={<PermissionsForm />}
        />

        <Route
            path="role-permissions/:id"
            element={<RolePermissionsPage />}
        />

        <Route
            path="user-roles/:id"
            element={<UserRolesPage />}
        />

    </>
);


export default accessControlRoutes;