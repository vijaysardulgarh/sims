import CrudListPage from '../../../shared/components/crud/CrudListPage';

const BuildingsListPage = () => {

    const columns = [

        {
            key: 'id',
            label: 'ID',
        },

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'code',
            label: 'Code',
        },

        {
            key: 'number_of_floors',
            label: 'Floors',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (

        <CrudListPage
            title="Buildings"
            endpoint="/infrastructure/buildings/"
            columns={columns}
            addPath="/dashboard/infrastructure/buildings/add"
            editPath="/dashboard/infrastructure/buildings/edit"
        />
    );
};

export default BuildingsListPage;