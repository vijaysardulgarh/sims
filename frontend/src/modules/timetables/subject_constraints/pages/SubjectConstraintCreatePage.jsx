import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import SubjectConstraintForm
    from '../components/SubjectConstraintForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/subjectConstraintService';

const SubjectConstraintCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Subject Constraint"

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

export default SubjectConstraintCreatePage;