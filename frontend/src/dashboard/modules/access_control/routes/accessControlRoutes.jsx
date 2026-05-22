import { Route } from "react-router-dom";


// =====================================
// ROLE PAGES
// =====================================

import RolesListPage from "../pages/roles/RolesListPage";

import AddRolePage from "../pages/roles/AddRolePage";

import EditRolePage from "../pages/roles/EditRolePage";


// =====================================
// USER PAGES
// =====================================

import UsersListPage from "../pages/users/UsersListPage";

import AddUserPage from "../pages/users/AddUserPage";

import EditUserPage from "../pages/users/EditUserPage";

import UserProfilePage from "../pages/users/UserProfilePage";


// =====================================
// ACCESS CONTROL PAGES
// =====================================

import AccessControlListPage from "../profiles/AccessControlListPage";

import AddAccessControlPage from "../profiles/AddAccessControlPage";

import EditAccessControlPage from "../profiles/EditAccessControlPage";


// =====================================
// PERMISSION PAGES
// =====================================

import PermissionsListPage from "../pages/permissions/PermissionsListPage";

import PermissionsForm from "../forms/PermissionsForm";

import RolePermissionsPage from "../pages/permissions/RolePermissionsPage";


// =====================================
// USER ROLE PAGES
// =====================================

import UserRolesListPage from "../pages/user_roles/UserRolesListPage";

import AddUserRolePage from "../pages/user_roles/AddUserRolePage";

import EditUserRolePage from "../pages/user_roles/EditUserRolePage";


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
        {/* ACCESS CONTROLS CRUD */}
        {/* ================================= */}

        <Route
            path="access-controls"
            element={<AccessControlListPage />}
        />

        <Route
            path="access-controls/add"
            element={<AddAccessControlPage />}
        />

        <Route
            path="access-controls/edit/:id"
            element={<EditAccessControlPage />}
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

    </>
);

export default accessControlRoutes;