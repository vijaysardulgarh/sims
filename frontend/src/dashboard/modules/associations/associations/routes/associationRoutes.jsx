// ============================================
// IMPORTS
// ============================================

import { Route } from 'react-router-dom';

import AssociationListPage from '../pages/AssociationListPage';
import AssociationCreatePage from '../pages/AssociationCreatePage';
import AssociationEditPage from '../pages/AssociationEditPage';
import AssociationDetailPage from '../pages/AssociationDetailPage';

// ============================================
// ROUTES
// ============================================

const associationRoutes = (

    <>

        <Route
            path="associations/associations"
            element={<AssociationListPage />}
        />

        <Route
            path="associations/associations/create"
            element={<AssociationCreatePage />}
        />

        <Route
            path="associations/associations/edit/:id"
            element={<AssociationEditPage />}
        />

        <Route
            path="associations/associations/:id"
            element={<AssociationDetailPage />}
        />

    </>

);

export default associationRoutes;