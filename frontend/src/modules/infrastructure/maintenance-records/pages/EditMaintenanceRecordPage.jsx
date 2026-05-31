import CrudEditPage from '../../../../shared/components/common/crud/CrudEditPage';

import MaintenanceRecordForm from '../components/MaintenanceRecordForm';

const EditMaintenanceRecordPage = () => {

    return (
        <CrudEditPage
            title="Edit Maintenance Record"
            endpoint="/infrastructure/maintenance-records/"
            FormComponent={MaintenanceRecordForm}
            redirectPath="/dashboard/infrastructure/maintenance-records"
        />
    );
};

export default EditMaintenanceRecordPage;