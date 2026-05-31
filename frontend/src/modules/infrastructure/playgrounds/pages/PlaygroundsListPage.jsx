import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const PlaygroundsListPage = () => {

    const columns = [

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'playground_type',
            label: 'Type',
        },

        {
            key: 'area',
            label: 'Area',
        },

        {
            key: 'capacity',
            label: 'Capacity',
        },

        {
            key: 'covered',
            label: 'Covered',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Playgrounds"
            endpoint="/infrastructure/playgrounds/"
            columns={columns}
            addPath="/dashboard/infrastructure/playgrounds/add"
            editPath="/dashboard/infrastructure/playgrounds/edit"
        />
    );
};

export default PlaygroundsListPage;