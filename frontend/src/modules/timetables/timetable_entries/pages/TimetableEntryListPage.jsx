import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/timetableEntryService';

const TimetableEntryListPage = () => {

    const columns = [

        {
            key: 'timetable_name',
            label: 'Timetable',
        },

        {
            key: 'day',
            label: 'Day',
        },

        {
            key: 'period_name',
            label: 'Period',
        },

        {
            key: 'subject_name',
            label: 'Subject',
        },

        {
            key: 'teacher_name',
            label: 'Teacher',
        },

        {
            key: 'remarks',
            label: 'Remarks',
        },

    ];

    return (

        <CrudListPage

            title="Timetable Entries"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TimetableEntryListPage;