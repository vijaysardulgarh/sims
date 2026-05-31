import CrudCreatePage from '../../../../shared/components/common/crud/CrudCreatePage';

import FacilityForm from '../components/FacilityForm';

const AddFacilityPage = () => {

    return (
        <CrudCreatePage
            title="Add Facility"
            endpoint="/infrastructure/facilities/"
            FormComponent={FacilityForm}
            redirectPath="/dashboard/infrastructure/facilities"
        />
    );
};

export default AddFacilityPage;