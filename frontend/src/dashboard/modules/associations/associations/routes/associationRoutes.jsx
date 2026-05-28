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

        {/* ================================= */}
        {/* ASSOCIATION LIST */}
        {/* ================================= */}

        <Route
            path="associations"
            element={<AssociationListPage />}
        />

        {/* ================================= */}
        {/* CREATE */}
        {/* ================================= */}

        <Route
            path="associations/create"
            element={<AssociationCreatePage />}
        />

        {/* ================================= */}
        {/* EDIT */}
        {/* ================================= */}

        <Route
            path="associations/edit/:id"
            element={<AssociationEditPage />}
        />

        {/* ================================= */}
        {/* DETAIL */}
        {/* ================================= */}

        <Route
            path="associations/:id"
            element={<AssociationDetailPage />}
        />

    </>
);

// ============================================
// EXPORT
// ============================================

export default associationRoutes;