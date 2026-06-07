import CrudEditPage from '../../../shared/components/crud/CrudEditPage';
import FacilityForm from '../components/FacilityForm';

const EditFacilityPage = () => {

    return (
        <CrudEditPage
            title="Edit Facility"
            endpoint="/infrastructure/facilities/"
            FormComponent={FacilityForm}
            redirectPath="/dashboard/infrastructure/facilities"
        />
    );
};

export default EditFacilityPage;