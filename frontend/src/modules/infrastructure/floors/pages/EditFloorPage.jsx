import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import FloorForm from '../components/FloorForm';

const EditFloorPage = () => {

    return (

        <CrudEditPage
            title="Edit Floor"
            endpoint="/infrastructure/floors/"
            FormComponent={FloorForm}
            redirectPath="/dashboard/infrastructure/floors"
        />
    );
};

export default EditFloorPage;