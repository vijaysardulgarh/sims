import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import SubjectRequirementForm
    from '../components/SubjectRequirementForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/subjectRequirementService';

const SubjectRequirementEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Subject Requirement"

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

export default SubjectRequirementEditPage;