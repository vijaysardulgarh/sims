import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/teacherWorkloadService';

const TeacherWorkloadListPage = () => {

    const columns = [

        {
            key: 'teacher',
            label: 'Teacher',
        },

        {
            key: 'maximum_periods_per_day',
            label: 'Max Periods/Day',
        },

        {
            key: 'maximum_periods_per_week',
            label: 'Max Periods/Week',
        },

        {
            key: 'minimum_periods_per_week',
            label: 'Min Periods/Week',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Teacher Workloads"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TeacherWorkloadListPage;