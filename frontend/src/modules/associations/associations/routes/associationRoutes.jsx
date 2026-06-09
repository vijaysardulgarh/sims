// ============================================
// IMPORTS
// ============================================

import { Route } from 'react-router-dom';

import AssociationListPage from '../pages/AssociationListPage';
import AssociationAddPage from '../pages/AssociationAddPage';
import AssociationEditPage from '../pages/AssociationEditPage';


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
            path="associations/associations/add"
            element={<AssociationAddPage />}
        />

        <Route
            path="associations/associations/edit/:id"
            element={<AssociationEditPage />}
        />

    </>

);

export default associationRoutes;