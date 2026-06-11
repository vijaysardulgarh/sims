import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
} from '../services/timetableAuditLogService';

const TimetableAuditLogListPage = () => {

    const columns = [

        {
            key: 'timetable',
            label: 'Timetable',
        },

        {
            key: 'action',
            label: 'Action',
        },

        {
            key: 'performed_by',
            label: 'Performed By',
        },

        {
            key: 'performed_at',
            label: 'Performed At',
        },

        {
            key: 'remarks',
            label: 'Remarks',
        },

    ];

    return (

        <CrudListPage

            title="Timetable Audit Logs"

            endpoint={ENDPOINT}

            columns={columns}

        />

    );

};

export default TimetableAuditLogListPage;