import CrudEditPage from '../../../../shared/components/crud/CrudEditPage';

import AnnouncementForm from '../components/AnnouncementForm';

const EditAnnouncementPage = () => {

    return (
        <CrudEditPage
            title="Edit Announcement"
            endpoint="/communications/announcements/"
            FormComponent={AnnouncementForm}
            redirectPath="/dashboard/communications/announcements"
        />
    );
};

export default EditAnnouncementPage;