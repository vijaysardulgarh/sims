import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/teacherAvailabilityService';

const TeacherAvailabilityListPage = () => {

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
            key: 'available_from',
            label: 'Available From',
        },

        {
            key: 'available_to',
            label: 'Available To',
        },

        {
            key: 'availability_type',
            label: 'Type',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Teacher Availabilities"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TeacherAvailabilityListPage;