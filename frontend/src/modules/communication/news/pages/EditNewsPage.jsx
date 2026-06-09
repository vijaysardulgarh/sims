import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import NewsForm from '../components/NewsForm';

const EditNewsPage = () => {

    return (
        <CrudEditPage
            title="Edit News"
            endpoint="/communications/news/"
            FormComponent={NewsForm}
            redirectPath="/dashboard/communications/news"
        />
    );
};

export default EditNewsPage;