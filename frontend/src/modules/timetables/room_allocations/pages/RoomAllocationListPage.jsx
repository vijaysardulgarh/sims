import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/roomAllocationService';

const RoomAllocationListPage = () => {

    const columns = [

        {
            key: 'timetable_entry',
            label: 'Timetable Entry',
        },

        {
            key: 'room',
            label: 'Room',
        },

        {
            key: 'allocation_date',
            label: 'Allocation Date',
        },

        {
            key: 'start_time',
            label: 'Start Time',
        },

        {
            key: 'end_time',
            label: 'End Time',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Room Allocations"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default RoomAllocationListPage;