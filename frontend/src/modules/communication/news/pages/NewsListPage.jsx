import CrudListPage from '../../../shared/components/crud/CrudListPage';

const NewsListPage = () => {

    const columns = [

        {
            key: 'title',
            label: 'Title',
        },

        {
            key: 'published_date',
            label: 'Published Date',
        },

        {
            key: 'is_published',
            label: 'Published',
        },
    ];

    return (
        <CrudListPage
            title="News"
            endpoint="/communications/news/"
            columns={columns}
            addPath="/dashboard/communications/news/add"
            editPath="/dashboard/communications/news/edit"
        />
    );
};

export default NewsListPage;