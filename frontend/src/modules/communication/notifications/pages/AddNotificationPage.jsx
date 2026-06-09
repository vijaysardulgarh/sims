import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import NotificationForm from '../components/NotificationForm';

const AddNotificationPage = () => {

    return (
        <CrudCreatePage
            title="Add Notification"
            endpoint="/communications/notifications/"
            FormComponent={NotificationForm}
            redirectPath="/dashboard/communications/notifications"
        />
    );
};

export default AddNotificationPage;