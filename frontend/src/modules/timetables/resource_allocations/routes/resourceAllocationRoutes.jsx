import {
    Route,
} from "react-router-dom";

import ResourceAllocationListPage
    from "../pages/ResourceAllocationListPage";

import ResourceAllocationCreatePage
    from "../pages/ResourceAllocationCreatePage";

import ResourceAllocationEditPage
    from "../pages/ResourceAllocationEditPage";

const resourceAllocationRoutes = (

    <Route path="resource-allocations">

        <Route
            index
            element={
                <ResourceAllocationListPage />
            }
        />

        <Route
            path="add"
            element={
                <ResourceAllocationCreatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <ResourceAllocationEditPage />
            }
        />

    </Route>

);

export default resourceAllocationRoutes;