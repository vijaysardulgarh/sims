import { Route } from 'react-router-dom';

import AssociationRoleListPage from '../pages/AssociationRoleListPage';
import AssociationRoleAddPage from '../pages/AssociationRoleAddPage';
import AssociationRoleEditPage from '../pages/AssociationRoleEditPage';

const associationRoleRoutes = (

    <>

        <Route
            path="associations/association-roles"
            element={<AssociationRoleListPage />}
        />

        <Route
            path="associations/association-roles/add"
            element={<AssociationRoleAddPage />}
        />

        <Route
            path="associations/association-roles/edit/:id"
            element={<AssociationRoleEditPage />}
        />

    </>

);

export default associationRoleRoutes;