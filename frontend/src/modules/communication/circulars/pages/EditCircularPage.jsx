import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import CircularForm from '../components/CircularForm';

const EditCircularPage = () => {

    return (
        <CrudEditPage
            title="Edit Circular"
            endpoint="/communications/circulars/"
            FormComponent={CircularForm}
            redirectPath="/dashboard/communications/circulars"
        />
    );
};

export default EditCircularPage;