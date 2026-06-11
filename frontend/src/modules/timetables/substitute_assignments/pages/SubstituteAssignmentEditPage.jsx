import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import SubstituteAssignmentForm
    from '../components/SubstituteAssignmentForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/substituteAssignmentService';

const SubstituteAssignmentEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Substitute Assignment"

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

export default SubstituteAssignmentEditPage;