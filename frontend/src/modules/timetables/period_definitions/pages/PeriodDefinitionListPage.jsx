import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/periodDefinitionService';

const PeriodDefinitionListPage = () => {

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
            key: 'start_time',
            label: 'Start Time',
        },

        {
            key: 'end_time',
            label: 'End Time',
        },

        {
            key: 'period_type',
            label: 'Type',
        },

        {
            key: 'display_order',
            label: 'Order',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Period Definitions"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default PeriodDefinitionListPage;