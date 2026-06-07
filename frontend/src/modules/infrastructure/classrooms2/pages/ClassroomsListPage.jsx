import CrudListPage from '../../../shared/components/crud/CrudListPage';

const ClassroomsListPage = () => {

    const columns = [

        {
            key: 'id',
            label: 'ID',
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
            key: 'classroom_code',
            label: 'Classroom Code',
        },

        {
            key: 'smart_classroom',
            label: 'Smart',
        },

        {
            key: 'air_conditioned',
            label: 'AC',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Classrooms"
            endpoint="/infrastructure/classrooms/"
            columns={columns}
            addPath="/dashboard/infrastructure/classrooms/add"
            editPath="/dashboard/infrastructure/classrooms/edit"
        />
    );
};

export default ClassroomsListPage;