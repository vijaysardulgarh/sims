import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import AssetCategoryForm from '../components/AssetCategoryForm';

const EditAssetCategoryPage = () => {

    return (
        <CrudEditPage
            title="Edit Asset Category"
            endpoint="/infrastructure/asset-categories/"
            FormComponent={AssetCategoryForm}
            redirectPath="/dashboard/infrastructure/asset-categories"
        />
    );
};

export default EditAssetCategoryPage;