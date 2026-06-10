import CrudListPage from '../../../shared/components/crud/CrudListPage';

const CircularsListPage = () => {

    const columns = [

        {
            key: 'reference_number',
            label: 'Reference No.',
        },

        {
            key: 'title',
            label: 'Title',
        },

        {
            key: 'issue_date',
            label: 'Issue Date',
        },

        {
            key: 'circular_type',
            label: 'Type',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage
            title="Circulars"
            endpoint="/communications/circulars/"
            columns={columns}
            addPath="/dashboard/communications/circulars/add"
            editPath="/dashboard/communications/circulars/edit"
        />

    );

};

export default CircularsListPage;