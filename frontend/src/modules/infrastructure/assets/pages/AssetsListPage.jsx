import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const AssetsListPage = () => {

    const columns = [

        {
            key: 'asset_code',
            label: 'Code',
        },

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'category_name',
            label: 'Category',
        },

        {
            key: 'quantity',
            label: 'Qty',
        },

        {
            key: 'location',
            label: 'Location',
        },

        {
            key: 'status',
            label: 'Status',
        },
    ];

    return (
        <CrudListPage
            title="Assets"
            endpoint="/infrastructure/assets/"
            columns={columns}
            addPath="/dashboard/infrastructure/assets/add"
            editPath="/dashboard/infrastructure/assets/edit"
        />
    );
};

export default AssetsListPage;