import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import CircularForm from '../components/CircularForm';

const AddCircularPage = () => {

    return (
        <CrudCreatePage
            title="Add Circular"
            endpoint="/communications/circulars/"
            FormComponent={CircularForm}
            redirectPath="/dashboard/communications/circulars"
        />
    );
};

export default AddCircularPage;