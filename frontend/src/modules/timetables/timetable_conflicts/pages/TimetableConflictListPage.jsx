import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/timetableConflictService';

const TimetableConflictListPage = () => {

    const columns = [

        {
            key: 'conflict_type',
            label: 'Conflict Type',
        },

        {
            key: 'timetable',
            label: 'Timetable',
        },

        {
            key: 'teacher',
            label: 'Teacher',
        },

        {
            key: 'room',
            label: 'Room',
        },

        {
            key: 'period',
            label: 'Period',
        },

        {
            key: 'severity',
            label: 'Severity',
        },

        {
            key: 'status',
            label: 'Status',
        },

    ];

    return (

        <CrudListPage

            title="Timetable Conflicts"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TimetableConflictListPage;