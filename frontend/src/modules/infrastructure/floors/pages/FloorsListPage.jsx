import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const FloorsListPage = () => {

    const columns = [

        {
            key: 'id',
            label: 'ID',
        },

        {
            key: 'building_name',
            label: 'Building',
        },

        {
            key: 'name',
            label: 'Floor Name',
        },

        {
            key: 'floor_number',
            label: 'Floor Number',
        },
    ];

    return (

        <CrudListPage
            title="Floors"
            endpoint="/infrastructure/floors/"
            columns={columns}
            addPath="/dashboard/infrastructure/floors/add"
            editPath="/dashboard/infrastructure/floors/edit"
        />
    );
};

export default FloorsListPage;