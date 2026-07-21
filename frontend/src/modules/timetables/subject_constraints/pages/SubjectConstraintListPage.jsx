import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
} from '../services/subjectConstraintService';


const SubjectConstraintListPage = () => {

    const columns = [

        {
            key: 'school_class',
            label: 'Class',
        },

        {
            key: 'section',
            label: 'Section',
        },

        {
            key: 'subject',
            label: 'Subject',
        },

        {
            key: 'theory_periods_per_week',
            label: 'Theory/Wk',
        },

        {
            key: 'lab_periods_per_week',
            label: 'Lab/Wk',
        },

        {
            key: 'total_periods_per_week',
            label: 'Total/Wk',
        },

        {
            key: 'is_compulsory',
            label: 'Compulsory',
            type: 'boolean',
        },

        {
            key: 'priority',
            label: 'Priority',
        },

        {
            key: 'max_periods_per_day',
            label: 'Max/Day',
        },

        {
            key: 'allow_consecutive_periods',
            label: 'Consecutive',
            type: 'boolean',
        },

        {
            key: 'required_consecutive_periods',
            label: 'Req. Consecutive',
        },

        {
            key: 'spread_across_week',
            label: 'Spread Week',
            type: 'boolean',
        },

        {
            key: 'avoid_first_period',
            label: 'Avoid First',
            type: 'boolean',
        },

        {
            key: 'avoid_last_period',
            label: 'Avoid Last',
            type: 'boolean',
        },

        {
            key: 'preferred_time_slot',
            label: 'Time Slot',
        },

        {
            key: 'is_active',
            label: 'Active',
            type: 'boolean',
        },

    ];

    return (

        <CrudListPage

            title="Subject Constraints"

            endpoint={ENDPOINT}

            columns={columns}

            editable={true}

            allowAddRow={true}

            allowDelete={true}

            allowBulkSave={true}

            allowImport={true}

            allowExport={true}

        />

    );

};

export default SubjectConstraintListPage;