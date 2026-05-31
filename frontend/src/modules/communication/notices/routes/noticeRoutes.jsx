import { Route } from 'react-router-dom';

import NoticesListPage from '../pages/NoticesListPage';
import AddNoticePage from '../pages/AddNoticePage';
import EditNoticePage from '../pages/EditNoticePage';

const noticeRoutes = (

    <Route path="notices">

        <Route
            index
            element={<NoticesListPage />}
        />

        <Route
            path="add"
            element={<AddNoticePage />}
        />

        <Route
            path="edit/:id"
            element={<EditNoticePage />}
        />

    </Route>
);

export default noticeRoutes;