import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/timetableService';

const TimetableListPage = () => {

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
            key: 'academic_session',
            label: 'Session',
        },

        {
            key: 'effective_from',
            label: 'Effective From',
        },

        {
            key: 'effective_to',
            label: 'Effective To',
        },

        {
            key: 'status',
            label: 'Status',
        },

        {
            key: 'is_published',
            label: 'Published',
        },

    ];

    return (

        <CrudListPage

            title="Timetables"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TimetableListPage;