import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import AssetForm from '../components/AssetForm';

const AddAssetPage = () => {

    return (
        <CrudCreatePage
            title="Add Asset"
            endpoint="/infrastructure/assets/"
            FormComponent={AssetForm}
            redirectPath="/dashboard/infrastructure/assets"
        />
    );
};

export default AddAssetPage;