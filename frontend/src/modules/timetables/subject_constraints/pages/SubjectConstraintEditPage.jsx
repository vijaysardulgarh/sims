import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import SubjectConstraintForm
    from '../components/SubjectConstraintForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/subjectConstraintService';

const SubjectConstraintEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Subject Constraint"

            endpoint={ENDPOINT}

            FormComponent={
                SubjectConstraintForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default SubjectConstraintEditPage;