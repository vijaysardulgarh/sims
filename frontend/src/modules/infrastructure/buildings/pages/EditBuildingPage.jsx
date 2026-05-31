import CrudEditPage from '../../../../components/common/crud/CrudEditPage';

import BuildingForm from '../components/BuildingForm';

const EditBuildingPage = () => {

    return (

        <CrudEditPage
            title="Edit Building"
            endpoint="/infrastructure/buildings/"
            FormComponent={BuildingForm}
            redirectPath="/dashboard/infrastructure/buildings"
        />
    );
};

export default EditBuildingPage;