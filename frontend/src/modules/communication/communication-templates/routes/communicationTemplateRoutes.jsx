import { Route } from 'react-router-dom';

import CommunicationTemplatesListPage from '../pages/CommunicationTemplatesListPage';
import AddCommunicationTemplatePage from '../pages/AddCommunicationTemplatePage';
import EditCommunicationTemplatePage from '../pages/EditCommunicationTemplatePage';

const communicationTemplateRoutes = (

    <Route path="communication-templates">

        <Route
            index
            element={
                <CommunicationTemplatesListPage />
            }
        />

        <Route
            path="add"
            element={
                <AddCommunicationTemplatePage />
            }
        />

        <Route
            path="edit/:id"
            element={
                <EditCommunicationTemplatePage />
            }
        />

    </Route>
);

export default communicationTemplateRoutes;