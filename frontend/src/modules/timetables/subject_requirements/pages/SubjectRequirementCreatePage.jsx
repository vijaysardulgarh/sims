import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import SubjectRequirementForm
    from '../components/SubjectRequirementForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/subjectRequirementService';

const SubjectRequirementCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Subject Requirement"

            endpoint={ENDPOINT}

            FormComponent={
                SubjectRequirementForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default SubjectRequirementCreatePage;