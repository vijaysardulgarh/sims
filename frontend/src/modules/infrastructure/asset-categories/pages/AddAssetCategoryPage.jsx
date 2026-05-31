import CrudCreatePage from '../../../../shared/components/common/crud/CrudCreatePage';

import AssetCategoryForm from '../components/AssetCategoryForm';

const AddAssetCategoryPage = () => {

    return (
        <CrudCreatePage
            title="Add Asset Category"
            endpoint="/infrastructure/asset-categories/"
            FormComponent={AssetCategoryForm}
            redirectPath="/dashboard/infrastructure/asset-categories"
        />
    );
};

export default AddAssetCategoryPage;