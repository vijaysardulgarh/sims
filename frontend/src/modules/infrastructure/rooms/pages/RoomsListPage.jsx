import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';


const RoomsListPage = () => {

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
            key: 'floor_name',
            label: 'Floor',
        },

        {
            key: 'room_number',
            label: 'Room Number',
        },

        {
            key: 'room_name',
            label: 'Room Name',
        },

        {
            key: 'room_type',
            label: 'Type',
        },

        {
            key: 'capacity',
            label: 'Capacity',
        },
    ];

    return (

        <CrudListPage
            title="Rooms"
            endpoint="/infrastructure/rooms/"
            columns={columns}
            addPath="/dashboard/infrastructure/rooms/add"
            editPath="/dashboard/infrastructure/rooms/edit"
        />
    );
};

export default RoomsListPage;