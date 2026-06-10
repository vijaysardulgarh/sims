import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import RecognitionForm
    from '../components/RecognitionForm';

const RecognitionCreatePage = () => {

    return (

        <CrudCreatePage
            title="Create Recognition"
            endpoint="/compliance/recognitions/"
            FormComponent={RecognitionForm}
            redirectPath="/dashboard/compliance/recognitions"
        />

    );

};

export default RecognitionCreatePage;