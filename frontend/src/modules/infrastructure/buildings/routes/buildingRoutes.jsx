import { Route } from 'react-router-dom';

import BuildingsListPage
    from '../pages/BuildingsListPage';

import AddBuildingPage
    from '../pages/AddBuildingPage';

import EditBuildingPage
    from '../pages/EditBuildingPage';

const buildingRoutes = (

    <Route path="buildings">

        <Route
            index
            element={
                <BuildingsListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddBuildingPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditBuildingPage />
            }
        />

    </Route>
);

export default buildingRoutes;