import CrudCreatePage from '../../../../shared/components/common/crud/CrudCreatePage';

import PlaygroundForm from '../components/PlaygroundForm';

const AddPlaygroundPage = () => {

    return (
        <CrudCreatePage
            title="Add Playground"
            endpoint="/infrastructure/playgrounds/"
            FormComponent={PlaygroundForm}
            redirectPath="/dashboard/infrastructure/playgrounds"
        />
    );
};

export default AddPlaygroundPage;