import { Route } from 'react-router-dom';

import NewsListPage from '../pages/NewsListPage';
import AddNewsPage from '../pages/AddNewsPage';
import EditNewsPage from '../pages/EditNewsPage';

const newsRoutes = (

    <Route path="news">

        <Route
            index
            element={<NewsListPage />}
        />

        <Route
            path="add"
            element={<AddNewsPage />}
        />

        <Route
            path="edit/:id"
            element={<EditNewsPage />}
        />

    </Route>
);

export default newsRoutes;