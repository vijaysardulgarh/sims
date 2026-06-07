import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import PlaygroundForm from '../components/PlaygroundForm';

const EditPlaygroundPage = () => {

    return (
        <CrudEditPage
            title="Edit Playground"
            endpoint="/infrastructure/playgrounds/"
            FormComponent={PlaygroundForm}
            redirectPath="/dashboard/infrastructure/playgrounds"
        />
    );
};

export default EditPlaygroundPage;