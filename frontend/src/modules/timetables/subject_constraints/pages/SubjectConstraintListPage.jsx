import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/subjectConstraintService';

const SubjectConstraintListPage = () => {

    const columns = [

        {
            key: 'subject',
            label: 'Subject',
        },

        {
            key: 'constraint_type',
            label: 'Constraint Type',
        },

        {
            key: 'value',
            label: 'Value',
        },

        {
            key: 'is_mandatory',
            label: 'Mandatory',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Subject Constraints"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default SubjectConstraintListPage;