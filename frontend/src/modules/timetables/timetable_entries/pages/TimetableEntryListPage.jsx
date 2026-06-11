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
            key: 'timetable',
            label: 'Timetable',
        },

        {
            key: 'day',
            label: 'Day',
        },

        {
            key: 'period',
            label: 'Period',
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
            key: 'subject',
            label: 'Subject',
        },

        {
            key: 'teacher',
            label: 'Teacher',
        },

        {
            key: 'room',
            label: 'Room',
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