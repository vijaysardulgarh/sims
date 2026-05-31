import CrudListPage from '../../../../shared/components/crud/CrudListPage';

const CommunicationTemplatesListPage = () => {

    const columns = [

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'category_name',
            label: 'Category',
        },

        {
            key: 'subject',
            label: 'Subject',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Communication Templates"
            endpoint="/communications/communication-templates/"
            columns={columns}
            addPath="/dashboard/communications/communication-templates/add"
            editPath="/dashboard/communications/communication-templates/edit"
        />
    );
};

export default CommunicationTemplatesListPage;