import { Route } from 'react-router-dom';

import MaintenanceRecordsListPage from '../pages/MaintenanceRecordsListPage';
import AddMaintenanceRecordPage from '../pages/AddMaintenanceRecordPage';
import EditMaintenanceRecordPage from '../pages/EditMaintenanceRecordPage';

const maintenanceRecordRoutes = (

    <Route path="maintenance-records">

        <Route
            index
            element={<MaintenanceRecordsListPage />}
        />

        <Route
            path="add"
            element={<AddMaintenanceRecordPage />}
        />

        <Route
            path="edit/:id"
            element={<EditMaintenanceRecordPage />}
        />

    </Route>
);

export default maintenanceRecordRoutes;