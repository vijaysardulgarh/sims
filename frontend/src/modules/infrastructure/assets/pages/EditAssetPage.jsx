import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import AssetForm from '../components/AssetForm';

const EditAssetPage = () => {

    return (
        <CrudEditPage
            title="Edit Asset"
            endpoint="/infrastructure/assets/"
            FormComponent={AssetForm}
            redirectPath="/dashboard/infrastructure/assets"
        />
    );
};

export default EditAssetPage;