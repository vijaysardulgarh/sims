import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/workingDayService';

const WorkingDayListPage = () => {

    const columns = [

        {
            key: 'day_name',
            label: 'Day',
        },

        {
            key: 'is_working_day',
            label: 'Working Day',
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

            title="Working Days"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default WorkingDayListPage;