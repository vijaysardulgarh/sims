import CrudEditPage from '../../../../shared/components/crud/CrudEditPage';

import CommunicationCategoryForm from '../components/CommunicationCategoryForm';

const EditCommunicationCategoryPage = () => {

    return (
        <CrudEditPage
            title="Edit Communication Category"
            endpoint="/communications/communication-categories/"
            FormComponent={CommunicationCategoryForm}
            redirectPath="/dashboard/communications/communication-categories"
        />
    );
};

export default EditCommunicationCategoryPage;