import CrudCreatePage from '../../../../shared/components/crud/CrudCreatePage';

import CommunicationCategoryForm from '../components/CommunicationCategoryForm';

const AddCommunicationCategoryPage = () => {

    return (
        <CrudCreatePage
            title="Add Communication Category"
            endpoint="/communications/communication-categories/"
            FormComponent={CommunicationCategoryForm}
            redirectPath="/dashboard/communications/communication-categories"
        />
    );
};

export default AddCommunicationCategoryPage;