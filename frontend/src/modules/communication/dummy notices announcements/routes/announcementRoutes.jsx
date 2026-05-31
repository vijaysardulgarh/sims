import { Route } from 'react-router-dom';

import AnnouncementsListPage from '../pages/AnnouncementsListPage';
import AddAnnouncementPage from '../pages/AddAnnouncementPage';
import EditAnnouncementPage from '../pages/EditAnnouncementPage';

const announcementRoutes = (

    <Route path="announcements">

        <Route
            index
            element={<AnnouncementsListPage />}
        />

        <Route
            path="add"
            element={<AddAnnouncementPage />}
        />

        <Route
            path="edit/:id"
            element={<EditAnnouncementPage />}
        />

    </Route>
);

export default announcementRoutes;