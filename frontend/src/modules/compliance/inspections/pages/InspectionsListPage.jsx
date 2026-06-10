import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

const InspectionsListPage = () => {

    const columns = [

        {
            key: 'inspection_type',
            label: 'Inspection Type',
        },

        {
            key: 'inspection_date',
            label: 'Date',
        },

        {
            key: 'authority',
            label: 'Authority',
        },

        {
            key: 'status',
            label: 'Status',
        },

    ];

    return (

        <CrudListPage
            title="Inspections"
            endpoint="/compliance/inspections/"
            columns={columns}
            addPath="/dashboard/compliance/inspections/create"
            editPath="/dashboard/compliance/inspections/edit"
        />

    );

};

export default InspectionsListPage;