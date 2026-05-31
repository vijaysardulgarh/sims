import CrudCreatePage from '../../../../shared/components/common/crud/CrudCreatePage';

import LaboratoryForm from '../components/LaboratoryForm';

const AddLaboratoryPage = () => {

    return (
        <CrudCreatePage
            title="Add Laboratory"
            endpoint="/infrastructure/laboratories/"
            FormComponent={LaboratoryForm}
            redirectPath="/dashboard/infrastructure/laboratories"
        />
    );
};

export default AddLaboratoryPage;