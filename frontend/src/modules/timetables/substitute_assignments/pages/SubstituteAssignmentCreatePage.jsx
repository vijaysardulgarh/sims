import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import SubstituteAssignmentForm
    from '../components/SubstituteAssignmentForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/substituteAssignmentService';

const SubstituteAssignmentCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Substitute Assignment"

            endpoint={ENDPOINT}

            FormComponent={
                SubstituteAssignmentForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default SubstituteAssignmentCreatePage;