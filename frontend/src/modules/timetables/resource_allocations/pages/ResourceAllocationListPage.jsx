import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/resourceAllocationService';

const ResourceAllocationListPage = () => {

    const columns = [

        {
            key: 'timetable_entry',
            label: 'Timetable Entry',
        },

        {
            key: 'resource',
            label: 'Resource',
        },

        {
            key: 'allocated_from',
            label: 'Allocated From',
        },

        {
            key: 'allocated_to',
            label: 'Allocated To',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Resource Allocations"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default ResourceAllocationListPage;