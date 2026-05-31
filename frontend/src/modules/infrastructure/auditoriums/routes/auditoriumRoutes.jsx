import { Route } from 'react-router-dom';

import AuditoriumsListPage
    from '../pages/AuditoriumsListPage';

import AddAuditoriumPage
    from '../pages/AddAuditoriumPage';

import EditAuditoriumPage
    from '../pages/EditAuditoriumPage';

const auditoriumRoutes = (

    <Route path="auditoriums">

        <Route
            index
            element={
                <AuditoriumsListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddAuditoriumPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditAuditoriumPage />
            }
        />

    </Route>
);

export default auditoriumRoutes;