import CrudCreatePage from '../../../../shared/components/common/crud/CrudCreatePage';

import BuildingForm from '../components/BuildingForm';

const AddBuildingPage = () => {

    return (

        <CrudCreatePage
            title="Add Building"
            endpoint="/infrastructure/buildings/"
            FormComponent={BuildingForm}
            redirectPath="/dashboard/infrastructure/buildings"
        />
    );
};

export default AddBuildingPage;