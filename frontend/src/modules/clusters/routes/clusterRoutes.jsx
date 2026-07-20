import { Route } from "react-router-dom";

import ClustersListPage from "../pages/ClustersListPage";
import ClusterCreatePage from "../pages/ClusterCreatePage";
import ClusterEditPage from "../pages/ClusterEditPage";
import ClusterViewPage from "../pages/ClusterViewPage";

const clusterRoutes = (

    <Route path="clusters">

        <Route
            index
            element={<ClustersListPage />}
        />

        <Route
            path="create"
            element={<ClusterCreatePage />}
        />

        <Route
            path=":id"
            element={<ClusterViewPage />}
        />

        <Route
            path="edit/:id"
            element={<ClusterEditPage />}
        />

    </Route>

);

export default clusterRoutes;