import { Route } from 'react-router-dom';

import AssociationMemberListPage from '../pages/AssociationMemberListPage';
import AssociationMemberCreatePage from '../pages/AssociationMemberCreatePage';
import AssociationMemberEditPage from '../pages/AssociationMemberEditPage';
import AssociationMemberDetailPage from '../pages/AssociationMemberDetailPage';

const associationMemberRoutes = (

    <>

        <Route
            path="associations/association_members"
            element={<AssociationMemberListPage />}
        />

        <Route
            path="associations/association_members/create"
            element={<AssociationMemberCreatePage />}
        />

        <Route
            path="associations/association_members/:id"
            element={<AssociationMemberDetailPage />}
        />

        <Route
            path="associations/association_members/edit/:id"
            element={<AssociationMemberEditPage />}
        />

    </>
);

export default associationMemberRoutes;