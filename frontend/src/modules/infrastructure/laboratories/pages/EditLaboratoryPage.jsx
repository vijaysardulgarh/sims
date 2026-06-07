import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import LaboratoryForm from '../components/LaboratoryForm';

const EditLaboratoryPage = () => {

    return (
        <CrudEditPage
            title="Edit Laboratory"
            endpoint="/infrastructure/laboratories/"
            FormComponent={LaboratoryForm}
            redirectPath="/dashboard/infrastructure/laboratories"
        />
    );
};

export default EditLaboratoryPage;