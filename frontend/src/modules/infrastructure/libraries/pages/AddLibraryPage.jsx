import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import LibraryForm from '../components/LibraryForm';

const AddLibraryPage = () => {

    return (
        <CrudCreatePage
            title="Add Library"
            endpoint="/infrastructure/libraries/"
            FormComponent={LibraryForm}
            redirectPath="/dashboard/infrastructure/libraries"
        />
    );
};

export default AddLibraryPage;