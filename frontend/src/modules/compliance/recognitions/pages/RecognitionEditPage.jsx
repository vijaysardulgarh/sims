import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import RecognitionForm
    from '../components/RecognitionForm';

const RecognitionEditPage = () => {

    return (

        <CrudEditPage
            title="Edit Recognition"
            endpoint="/compliance/recognitions/"
            FormComponent={RecognitionForm}
            redirectPath="/dashboard/compliance/recognitions"
        />

    );

};

export default RecognitionEditPage;