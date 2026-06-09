import CrudListPage from '../../../shared/components/crud/CrudListPage';

const CommunicationCategoriesListPage = () => {

    const columns = [

        {
            key: 'name',
            label: 'Name',
        },

        {
            key: 'code',
            label: 'Code',
        },

        {
            key: 'is_active',
            label: 'Active',
        },
    ];

    return (
        <CrudListPage
            title="Communication Categories"
            endpoint="/communications/communication-categories/"
            columns={columns}
            addPath="/dashboard/communications/communication-categories/add"
            editPath="/dashboard/communications/communication-categories/edit"
        />
    );
};

export default CommunicationCategoriesListPage;