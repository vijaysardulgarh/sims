import CrudListPage from '../../../../shared/components/crud/CrudListPage';

const AnnouncementsListPage = () => {

    const columns = [

        {
            key: 'title',
            label: 'Title',
        },

        {
            key: 'category_name',
            label: 'Category',
        },

        {
            key: 'publish_date',
            label: 'Publish Date',
        },

        {
            key: 'expiry_date',
            label: 'Expiry Date',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Announcements"
            endpoint="/communications/announcements/"
            columns={columns}
            addPath="/dashboard/communications/announcements/add"
            editPath="/dashboard/communications/announcements/edit"
        />
    );
};

export default AnnouncementsListPage;