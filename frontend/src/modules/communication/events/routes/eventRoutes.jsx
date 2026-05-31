import { Route } from 'react-router-dom';

import EventsListPage from '../pages/EventsListPage';
import AddEventPage from '../pages/AddEventPage';
import EditEventPage from '../pages/EditEventPage';

const eventRoutes = (

    <Route path="events">

        <Route
            index
            element={<EventsListPage />}
        />

        <Route
            path="add"
            element={<AddEventPage />}
        />

        <Route
            path="edit/:id"
            element={<EditEventPage />}
        />

    </Route>
);

export default eventRoutes;