import CrudListPage from '../../../../shared/components/crud/CrudListPage';

const NotificationsListPage = () => {

    const columns = [

        {
            key: 'subject',
            label: 'Subject',
        },

        {
            key: 'notification_type',
            label: 'Type',
        },

        {
            key: 'scheduled_at',
            label: 'Scheduled At',
        },

        {
            key: 'status',
            label: 'Status',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Notifications"
            endpoint="/communications/notifications/"
            columns={columns}
            addPath="/dashboard/communications/notifications/add"
            editPath="/dashboard/communications/notifications/edit"
        />
    );
};

export default NotificationsListPage;