// ============================================
// IMPORTS
// ============================================

import { Route } from 'react-router-dom';

import AssociationMeetingListPage from '../pages/AssociationMeetingListPage';

import AssociationMeetingCreatePage from '../pages/AssociationMeetingCreatePage';

import AssociationMeetingEditPage from '../pages/AssociationMeetingEditPage';

import AssociationMeetingDetailPage from '../pages/AssociationMeetingDetailPage';

// ============================================
// ROUTES
// ============================================

const associationMeetingRoutes = (

    <>

        <Route
            path="associations/association-meetings"
            element={<AssociationMeetingListPage />}
        />

        <Route
            path="associations/association-meetings/create"
            element={<AssociationMeetingCreatePage />}
        />

        <Route
            path="associations/association-meetings/edit/:id"
            element={<AssociationMeetingEditPage />}
        />

        <Route
            path="associations/association-meetings/:id"
            element={<AssociationMeetingDetailPage />}
        />

    </>
);

export default associationMeetingRoutes;