import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/teacherPreferenceService';

const TeacherPreferenceListPage = () => {

    const columns = [

        {
            key: 'teacher',
            label: 'Teacher',
        },

        {
            key: 'day',
            label: 'Day',
        },

        {
            key: 'preferred_period',
            label: 'Preferred Period',
        },

        {
            key: 'preference_level',
            label: 'Preference Level',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Teacher Preferences"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TeacherPreferenceListPage;