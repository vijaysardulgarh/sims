import CrudEditPage from '../../../../shared/components/common/crud/CrudEditPage';

import AcademicSessionForm from '../components/AcademicSessionForm';

const EditAcademicSessionPage = () => {

    return (

        <CrudEditPage
            title="Edit Academic Session"
            endpoint="/academics/sessions/"
            FormComponent={AcademicSessionForm}
            redirectPath="/dashboard/academics/sessions"
            successMessage="Academic session updated successfully."
        />

    );
};

export default EditAcademicSessionPage;