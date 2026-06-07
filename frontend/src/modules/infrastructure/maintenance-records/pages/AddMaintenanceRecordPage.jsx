import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import MaintenanceRecordForm from '../components/MaintenanceRecordForm';

const AddMaintenanceRecordPage = () => {

    return (
        <CrudCreatePage
            title="Add Maintenance Record"
            endpoint="/infrastructure/maintenance-records/"
            FormComponent={MaintenanceRecordForm}
            redirectPath="/dashboard/infrastructure/maintenance-records"
        />
    );
};

export default AddMaintenanceRecordPage;