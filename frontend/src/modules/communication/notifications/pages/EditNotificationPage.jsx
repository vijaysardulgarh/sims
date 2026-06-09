import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import NotificationForm from '../components/NotificationForm';

const EditNotificationPage = () => {

    return (
        <CrudEditPage
            title="Edit Notification"
            endpoint="/communications/notifications/"
            FormComponent={NotificationForm}
            redirectPath="/dashboard/communications/notifications"
        />
    );
};

export default EditNotificationPage;