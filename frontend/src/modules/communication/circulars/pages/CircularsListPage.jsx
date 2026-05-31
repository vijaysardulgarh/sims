import CrudListPage from '../../../../shared/components/crud/CrudListPage';

const CircularsListPage = () => {

    const columns = [

        {
            key: 'circular_number',
            label: 'Circular No.',
        },

        {
            key: 'title',
            label: 'Title',
        },

        {
            key: 'circular_date',
            label: 'Date',
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