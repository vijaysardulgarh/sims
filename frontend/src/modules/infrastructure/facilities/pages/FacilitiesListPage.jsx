import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const FacilitiesListPage = () => {

    const columns = [

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'facility_type',
            label: 'Type',
        },

        {
            key: 'installation_date',
            label: 'Installed On',
        },

        {
            key: 'available',
            label: 'Available',
        },
    ];

    return (
        <CrudListPage
            title="Facilities"
            endpoint="/infrastructure/facilities/"
            columns={columns}
            addPath="/dashboard/infrastructure/facilities/add"
            editPath="/dashboard/infrastructure/facilities/edit"
        />
    );
};

export default FacilitiesListPage;