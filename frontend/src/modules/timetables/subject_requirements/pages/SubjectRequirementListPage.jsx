import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/subjectRequirementService';

const SubjectRequirementListPage = () => {

    const columns = [

        {
            key: 'subject',
            label: 'Subject',
        },

        {
            key: 'school_class',
            label: 'Class',
        },

        {
            key: 'periods_per_week',
            label: 'Periods/Week',
        },

        {
            key: 'minimum_periods_per_day',
            label: 'Min/Day',
        },

        {
            key: 'maximum_periods_per_day',
            label: 'Max/Day',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Subject Requirements"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default SubjectRequirementListPage;