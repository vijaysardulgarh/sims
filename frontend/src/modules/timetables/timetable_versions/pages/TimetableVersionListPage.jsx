import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/timetableVersionService';

const TimetableVersionListPage = () => {

    const columns = [

        {
            key: 'timetable',
            label: 'Timetable',
        },

        {
            key: 'version_number',
            label: 'Version',
        },

        {
            key: 'version_name',
            label: 'Version Name',
        },

        {
            key: 'created_by',
            label: 'Created By',
        },

        {
            key: 'created_at',
            label: 'Created At',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Timetable Versions"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TimetableVersionListPage;