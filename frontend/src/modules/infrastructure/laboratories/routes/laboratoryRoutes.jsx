import { Route } from 'react-router-dom';

import LaboratoriesListPage
    from '../pages/LaboratoriesListPage';

import AddLaboratoryPage
    from '../pages/AddLaboratoryPage';

import EditLaboratoryPage
    from '../pages/EditLaboratoryPage';

const laboratoryRoutes = (

    <Route path="laboratories">

        <Route
            index
            element={
                <LaboratoriesListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddLaboratoryPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditLaboratoryPage />
            }
        />

    </Route>
);

export default laboratoryRoutes;