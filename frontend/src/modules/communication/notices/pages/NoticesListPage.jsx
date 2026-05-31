import CrudListPage from '../../../../shared/components/crud/CrudListPage';

const NoticesListPage = () => {

    const columns = [

        {
            key: 'notice_number',
            label: 'Notice No.',
        },

        {
            key: 'title',
            label: 'Title',
        },

        {
            key: 'notice_date',
            label: 'Notice Date',
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
            title="Notices"
            endpoint="/communications/notices/"
            columns={columns}
            addPath="/dashboard/communications/notices/add"
            editPath="/dashboard/communications/notices/edit"
        />
    );
};

export default NoticesListPage;