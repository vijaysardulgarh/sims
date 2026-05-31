
import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const LaboratoriesListPage = () => {

    const columns = [

        {
            key: 'lab_code',
            label: 'Lab Code',
        },

        {
            key: 'lab_type',
            label: 'Lab Type',
        },

        {
            key: 'room_number',
            label: 'Room',
        },

        {
            key: 'equipment_count',
            label: 'Equipment',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Laboratories"
            endpoint="/infrastructure/laboratories/"
            columns={columns}
            addPath="/dashboard/infrastructure/laboratories/add"
            editPath="/dashboard/infrastructure/laboratories/edit"
        />
    );
};

export default LaboratoriesListPage;