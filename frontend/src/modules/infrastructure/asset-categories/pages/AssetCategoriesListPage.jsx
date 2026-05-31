import CrudListPage from '../../../../shared/components/common/crud/CrudListPage';

const AssetCategoriesListPage = () => {

    const columns = [

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'code',
            label: 'Code',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Asset Categories"
            endpoint="/infrastructure/asset-categories/"
            columns={columns}
            addPath="/dashboard/infrastructure/asset-categories/add"
            editPath="/dashboard/infrastructure/asset-categories/edit"
        />
    );
};

export default AssetCategoriesListPage;