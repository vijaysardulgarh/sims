import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const AuditoriumsListPage = () => {

    const columns = [

        {
            key: 'auditorium_code',
            label: 'Code',
        },

        {
            key: 'room_number',
            label: 'Room',
        },

        {
            key: 'seating_capacity',
            label: 'Capacity',
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
            title="Auditoriums"
            endpoint="/infrastructure/auditoriums/"
            columns={columns}
            addPath="/dashboard/infrastructure/auditoriums/add"
            editPath="/dashboard/infrastructure/auditoriums/edit"
        />
    );
};

export default AuditoriumsListPage;