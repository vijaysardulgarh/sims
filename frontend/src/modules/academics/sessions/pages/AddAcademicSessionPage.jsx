import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import AcademicSessionForm from '../components/AcademicSessionForm';

const AddAcademicSessionPage = () => {

    const initialValues = {

        name: '',

        start_date: '',

        end_date: '',

        is_current: false,

    };

    return (

        <CrudCreatePage

            title="Add Academic Session"

            endpoint="/academics/sessions/"

            FormComponent={
                AcademicSessionForm
            }

            initialValues={
                initialValues
            }

            redirectPath="/dashboard/academics/sessions"

            successMessage="Academic session created successfully."

        />

    );
};

export default AddAcademicSessionPage;