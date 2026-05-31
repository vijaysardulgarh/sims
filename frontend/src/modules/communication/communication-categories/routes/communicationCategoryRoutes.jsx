import { Route } from 'react-router-dom';

import CommunicationCategoriesListPage from '../pages/CommunicationCategoriesListPage';
import AddCommunicationCategoryPage from '../pages/AddCommunicationCategoryPage';
import EditCommunicationCategoryPage from '../pages/EditCommunicationCategoryPage';

const communicationCategoryRoutes = (

    <Route path="communication-categories">

        <Route
            index
            element={
                <CommunicationCategoriesListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddCommunicationCategoryPage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditCommunicationCategoryPage />
            }
        />

    </Route>
);

export default communicationCategoryRoutes;