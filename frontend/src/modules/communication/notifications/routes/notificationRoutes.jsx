import { Route } from 'react-router-dom';

import NotificationsListPage from '../pages/NotificationsListPage';
import AddNotificationPage from '../pages/AddNotificationPage';
import EditNotificationPage from '../pages/EditNotificationPage';

const notificationRoutes = (

    <Route path="notifications">

        <Route
            index
            element={<NotificationsListPage />}
        />

        <Route
            path="add"
            element={<AddNotificationPage />}
        />

        <Route
            path="edit/:id"
            element={<EditNotificationPage />}
        />

    </Route>
);

export default notificationRoutes;