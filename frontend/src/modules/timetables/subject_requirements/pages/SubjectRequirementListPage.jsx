import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import { SubjectRequirementService } from "../services/subjectRequirementService";


const SubjectRequirementListPage = () => {

    const columns = [

        {
            key: 'school_class_name',
            label: 'Class',
            editable: false,
        },

        {
            key: 'section_name',
            label: 'Section',
            editable: false,
        },

        {
            key: 'stream_name',
            label: 'Stream',
            editable: false,
        },

        {
            key: 'sub_stream',
            label: 'Sub Stream',
        },

        {
            key: 'subject_name',
            label: 'Subject',
            editable: false,
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
            editable: false,
        },

        {
            key: 'requires_lab',
            label: 'Lab',
            type: 'boolean',
            editable: false,
        },

        {
            key: 'is_compulsory',
            label: 'Compulsory',
            type: 'boolean',
        },

        {
            key: 'is_shared',
            label: 'Shared',
            type: 'boolean',
        },

        {
            key: 'remarks',
            label: 'Remarks',
        },

        {
            key: 'is_active',
            label: 'Active',
            type: 'boolean',
        },

    ];

    return (

        <CrudListPage

            title="Subject Requirements"

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

export default SubjectRequirementListPage;