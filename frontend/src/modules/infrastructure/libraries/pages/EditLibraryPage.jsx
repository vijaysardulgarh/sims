import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import LibraryForm from '../components/LibraryForm';

const EditLibraryPage = () => {

    return (
        <CrudEditPage
            title="Edit Library"
            endpoint="/infrastructure/libraries/"
            FormComponent={LibraryForm}
            redirectPath="/dashboard/infrastructure/libraries"
        />
    );
};

export default EditLibraryPage;