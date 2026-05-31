import { Route } from 'react-router-dom';

import AssetCategoriesListPage
    from '../pages/AssetCategoriesListPage';

import AddAssetCategoryPage
    from '../pages/AddAssetCategoryPage';

import EditAssetCategoryPage
    from '../pages/EditAssetCategoryPage';

const assetCategoryRoutes = (

    <Route path="asset-categories">

        <Route
            index
            element={
                <AssetCategoriesListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddAssetCategoryPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditAssetCategoryPage />
            }
        />

    </Route>
);

export default assetCategoryRoutes;