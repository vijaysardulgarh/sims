import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/timetablePublicationService';

const TimetablePublicationListPage = () => {

    const columns = [

        {
            key: 'timetable',
            label: 'Timetable',
        },

        {
            key: 'publication_type',
            label: 'Publication Type',
        },

        {
            key: 'published_at',
            label: 'Published At',
        },

        {
            key: 'published_by',
            label: 'Published By',
        },

        {
            key: 'is_published',
            label: 'Published',
        },

    ];

    return (

        <CrudListPage

            title="Timetable Publications"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TimetablePublicationListPage;