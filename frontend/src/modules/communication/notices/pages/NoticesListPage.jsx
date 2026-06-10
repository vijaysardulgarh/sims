import CrudListPage from '../../../shared/components/crud/CrudListPage';

const NoticesListPage = () => {

    const columns = [

        {
            key: 'notice_type',
            label: 'Type',
        },

        {
            key: 'title',
            label: 'Title',
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
            key: 'is_published',
            label: 'Published',
        },

    ];

    return (

        <CrudListPage
            title="Notices"
            endpoint="/communications/notices/"
            columns={columns}
            addPath="/dashboard/communications/notices/add"
            editPath="/dashboard/communications/notices/edit"
        />

    );

};

export default NoticesListPage;