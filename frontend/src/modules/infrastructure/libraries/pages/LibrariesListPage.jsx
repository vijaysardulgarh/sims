import CrudListPage from '../../../shared/components/crud/CrudListPage';

const LibrariesListPage = () => {

    const columns = [

        {
            key: 'library_code',
            label: 'Library Code',
        },

        {
            key: 'room_number',
            label: 'Room',
        },

        {
            key: 'total_books',
            label: 'Books',
        },

        {
            key: 'seating_capacity',
            label: 'Capacity',
        },

        {
            key: 'digital_library',
            label: 'Digital',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Libraries"
            endpoint="/infrastructure/libraries/"
            columns={columns}
            addPath="/dashboard/infrastructure/libraries/add"
            editPath="/dashboard/infrastructure/libraries/edit"
        />
    );
};

export default LibrariesListPage;