import { Route } from 'react-router-dom';

import CircularsListPage from '../pages/CircularsListPage';
import AddCircularPage from '../pages/AddCircularPage';
import EditCircularPage from '../pages/EditCircularPage';

const circularRoutes = (

    <Route path="circulars">

        <Route
            index
            element={<CircularsListPage />}
        />

        <Route
            path="add"
            element={<AddCircularPage />}
        />

        <Route
            path="edit/:id"
            element={<EditCircularPage />}
        />

    </Route>
);

export default circularRoutes;