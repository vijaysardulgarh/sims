import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/timetableApprovalService';

const TimetableApprovalListPage = () => {

    const columns = [

        {
            key: 'timetable',
            label: 'Timetable',
        },

        {
            key: 'status',
            label: 'Status',
        },

        {
            key: 'approved_by',
            label: 'Approved By',
        },

        {
            key: 'approved_at',
            label: 'Approved At',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Timetable Approvals"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default TimetableApprovalListPage;