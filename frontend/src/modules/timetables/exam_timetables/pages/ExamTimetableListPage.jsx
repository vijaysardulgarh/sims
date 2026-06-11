import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/examTimetableService';

const ExamTimetableListPage = () => {

    const columns = [

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'code',
            label: 'Code',
        },

        {
            key: 'school_class',
            label: 'Class',
        },

        {
            key: 'section',
            label: 'Section',
        },

        {
            key: 'exam',
            label: 'Exam',
        },

        {
            key: 'effective_from',
            label: 'Effective From',
        },

        {
            key: 'is_published',
            label: 'Published',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Exam Timetables"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default ExamTimetableListPage;