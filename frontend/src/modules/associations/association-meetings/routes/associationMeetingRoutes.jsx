// ============================================
// IMPORTS
// ============================================

import { Route } from 'react-router-dom';

import AssociationMeetingListPage from '../pages/AssociationMeetingListPage';

import AssociationMeetingCreatePage from '../pages/AddAssociationMeeting';

import AssociationMeetingEditPage from '../pages/EditAssociationMeeting';
import AddAssociationMeeting from '../pages/AddAssociationMeeting';



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
            path="associations/association-meetings/add"
            element={<AddAssociationMeeting />}
        />

        <Route
            path="associations/association-meetings/edit/:id"
            element={<AssociationMeetingEditPage />}
        />


    </>
);

export default associationMeetingRoutes;