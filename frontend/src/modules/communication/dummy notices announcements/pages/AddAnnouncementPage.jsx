import CrudCreatePage from '../../../../shared/components/crud/CrudCreatePage';

import AnnouncementForm from '../components/AnnouncementForm';

const AddAnnouncementPage = () => {

    return (
        <CrudCreatePage
            title="Add Announcement"
            endpoint="/communications/announcements/"
            FormComponent={AnnouncementForm}
            redirectPath="/dashboard/communications/announcements"
        />
    );
};

export default AddAnnouncementPage;