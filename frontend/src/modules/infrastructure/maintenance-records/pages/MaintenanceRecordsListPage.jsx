import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const MaintenanceRecordsListPage = () => {

    const columns = [

        {
            key: 'asset_code',
            label: 'Asset Code',
        },

        {
            key: 'asset_name',
            label: 'Asset',
        },

        {
            key: 'maintenance_date',
            label: 'Date',
        },

        {
            key: 'service_type',
            label: 'Type',
        },

        {
            key: 'vendor_name',
            label: 'Vendor',
        },

        {
            key: 'cost',
            label: 'Cost',
        },
    ];

    return (
        <CrudListPage
            title="Maintenance Records"
            endpoint="/infrastructure/maintenance-records/"
            columns={columns}
            addPath="/dashboard/infrastructure/maintenance-records/add"
            editPath="/dashboard/infrastructure/maintenance-records/edit"
        />
    );
};

export default MaintenanceRecordsListPage;