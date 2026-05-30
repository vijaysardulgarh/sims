import { Route } from "react-router-dom";

import roleRoutes from
"../roles/routes/roleRoutes";

import userRoutes from
"../users/routes/userRoutes";

import permissionRoutes from
"../permissions/routes/permissionRoutes";

import rolePermissionRoutes from
"../role_permissions/routes/rolePermissionRoutes";

import systemModulesRoutes from
"../system-modules/routes/systemModulesRoutes";

import userRoleRoutes from
"../user_roles/routes/userRoleRoutes";

import userPermissionRoutes from
"../user_permissions/routes/userPermissionRoutes";


const accountsRoutes = (

    <Route path="accounts">

        {roleRoutes}

        {userRoutes}

        {permissionRoutes}

        {rolePermissionRoutes}

        {systemModulesRoutes}

        {userRoleRoutes}

        {userPermissionRoutes}

    </Route>

);

export default accountsRoutes;