// ============================================
// IMPORTS
// ============================================

import { Route } from 'react-router-dom';

import AssociationRoleListPage from '../pages/AssociationRoleListPage';
import AssociationRoleCreatePage from '../pages/AssociationRoleCreatePage';
import AssociationRoleEditPage from '../pages/AssociationRoleEditPage';
import AssociationRoleDetailPage from '../pages/AssociationRoleDetailPage';

// ============================================
// ROUTES
// ============================================

const associationRoleRoutes = (

    <>

        <Route
            path="associations/association-roles"
            element={<AssociationRoleListPage />}
        />

        <Route
            path="associations/association-roles/create"
            element={<AssociationRoleCreatePage />}
        />

        <Route
            path="associations/association-roles/:id"
            element={<AssociationRoleDetailPage />}
        />

        <Route
            path="associations/association-roles/edit/:id"
            element={<AssociationRoleEditPage />}
        />

    </>
);

export default associationRoleRoutes;