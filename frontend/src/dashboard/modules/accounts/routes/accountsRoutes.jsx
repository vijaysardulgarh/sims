// =========================================
// FILE:
// frontend/src/routes/accountsRoutes.jsx
// =========================================

import { Route } from "react-router-dom";


// =====================================
// ROLE PAGES
// =====================================

import RolesListPage from "../roles/pages/RolesListPage";

import AddRolePage from "../roles/pages/AddRolePage";

import EditRolePage from "../roles/pages/EditRolePage";


// =====================================
// USER PAGES
// =====================================

import UsersListPage from "../users/pages/UsersListPage";

import AddUserPage from "../users/pages/AddUserPage";

import EditUserPage from "../users/pages/EditUserPage";

import UserProfilePage from "../users/pages/UserProfilePage";


// =====================================
// PERMISSION PAGES
// =====================================

import PermissionsListPage from "../permissions/pages/PermissionsListPage";

import AddPermissionPage from "../permissions/pages/AddPermissionPage";

import EditPermissionPage from "../permissions/pages/EditPermissionPage";

import RolePermissionsPage from "../role_permissions/pages/RolePermissionsPage";


// =====================================
// MODULE PAGES
// =====================================

import ModulesListPage from "../modules/pages/ModulesListPage";

import AddModulePage from "../modules/pages/AddModulePage";

import EditModulePage from "../modules/pages/EditModulePage";


// =====================================
// USER ROLE PAGES
// =====================================

import UserRolesListPage from "../user_roles/pages/UserRolesListPage";

import AddUserRolePage from "../user_roles/pages/AddUserRolePage";

import EditUserRolePage from "../user_roles/pages/EditUserRolePage";


// =====================================
// USER PERMISSION PAGES
// =====================================

import UserPermissionsPage from "../user_permissions/pages/UserPermissionsPage";


// =====================================
// ROUTES
// =====================================

const accountsRoutes = (

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
            element={<AddPermissionPage />}
        />

        <Route
            path="permissions/edit/:id"
            element={<EditPermissionPage />}
        />

        <Route
            path="roles/:id/permissions"
            element={<RolePermissionsPage />}
        />


        {/* ================================= */}
        {/* MODULES */}
        {/* ================================= */}

        <Route
            path="modules"
            element={<ModulesListPage />}
        />

        <Route
            path="modules/add"
            element={<AddModulePage />}
        />

        <Route
            path="modules/edit/:id"
            element={<EditModulePage />}
        />


        {/* ================================= */}
        {/* USER ROLES */}
        {/* ================================= */}

        <Route
            path="user-roles"
            element={<UserRolesListPage />}
        />

        <Route
            path="user-roles/add"
            element={<AddUserRolePage />}
        />

        <Route
            path="user-roles/edit/:id"
            element={<EditUserRolePage />}
        />


        {/* ================================= */}
        {/* USER PERMISSIONS */}
        {/* ================================= */}

        <Route
            path="user-permissions"
            element={<UserPermissionsPage />}
        />

    </>
);

export default accountsRoutes;