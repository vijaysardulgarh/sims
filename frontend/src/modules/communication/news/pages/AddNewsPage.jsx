import CrudCreatePage from '../../../../shared/components/crud/CrudCreatePage';

import NewsForm from '../components/NewsForm';

const AddNewsPage = () => {

    return (
        <CrudCreatePage
            title="Add News"
            endpoint="/communications/news/"
            FormComponent={NewsForm}
            redirectPath="/dashboard/communications/news"
        />
    );
};

export default AddNewsPage;