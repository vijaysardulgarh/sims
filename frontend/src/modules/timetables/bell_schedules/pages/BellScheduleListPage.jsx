import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
} from '../services/bellScheduleService';

const BellScheduleListPage = () => {

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
            key: 'start_date',
            label: 'Start Date',
        },

        {
            key: 'end_date',
            label: 'End Date',
        },

        {
            key: 'is_default',
            label: 'Default',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Bell Schedules"

            endpoint={ENDPOINT}

            columns={columns}

            addPath="/dashboard/timetables/bell-schedules/add"

            editPath="/dashboard/timetables/bell-schedules/edit"

        />

    );

};

export default BellScheduleListPage;