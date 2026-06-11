import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/examTimetableEntryService';

const ExamTimetableEntryListPage = () => {

    const columns = [

        {
            key: 'exam_timetable',
            label: 'Exam Timetable',
        },

        {
            key: 'subject',
            label: 'Subject',
        },

        {
            key: 'exam_date',
            label: 'Exam Date',
        },

        {
            key: 'start_time',
            label: 'Start Time',
        },

        {
            key: 'end_time',
            label: 'End Time',
        },

        {
            key: 'room',
            label: 'Room',
        },

        {
            key: 'invigilator',
            label: 'Invigilator',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Exam Timetable Entries"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default ExamTimetableEntryListPage;