import { Route } from 'react-router-dom';

import AssetsListPage from '../pages/AssetsListPage';
import AddAssetPage from '../pages/AddAssetPage';
import EditAssetPage from '../pages/EditAssetPage';

const assetRoutes = (

    <Route path="assets">

        <Route
            index
            element={<AssetsListPage />}
        />

        <Route
            path="add"
            element={<AddAssetPage />}
        />

        <Route
            path="edit/:id"
            element={<EditAssetPage />}
        />

    </Route>
);

export default assetRoutes;