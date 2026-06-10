import { Route } from 'react-router-dom';

import InspectionsListPage
    from '../pages/InspectionsListPage';

import InspectionCreatePage
    from '../pages/InspectionCreatePage';

import InspectionEditPage
    from '../pages/InspectionEditPage';

const inspectionRoutes = (

    <>

        <Route
            path="inspections"
            element={
                <InspectionsListPage />
            }
        />

        <Route
            path="inspections/create"
            element={
                <InspectionCreatePage />
            }
        />

        <Route
            path="inspections/edit/:id"
            element={
                <InspectionEditPage />
            }
        />

    </>

);

export default inspectionRoutes;