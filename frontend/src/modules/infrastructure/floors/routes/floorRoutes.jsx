import { Route } from 'react-router-dom';

import FloorsListPage
from '../pages/FloorsListPage';

import AddFloorPage
from '../pages/AddFloorPage';

import EditFloorPage
from '../pages/EditFloorPage';

const floorRoutes = (

    <Route path="floors">

        <Route
            index
            element={
                <FloorsListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddFloorPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditFloorPage />
            }
        />

    </Route>
);

export default floorRoutes;