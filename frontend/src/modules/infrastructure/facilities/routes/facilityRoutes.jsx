import { Route } from 'react-router-dom';

import FacilitiesListPage
    from '../pages/FacilitiesListPage';

import AddFacilityPage
    from '../pages/AddFacilityPage';

import EditFacilityPage
    from '../pages/EditFacilityPage';

const facilityRoutes = (

    <Route path="facilities">

        <Route
            index
            element={
                <FacilitiesListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddFacilityPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditFacilityPage />
            }
        />

    </Route>
);

export default facilityRoutes;