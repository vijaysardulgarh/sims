import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import FloorForm from '../components/FloorForm';

const AddFloorPage = () => {

    return (

        <CrudCreatePage
            title="Add Floor"
            endpoint="/infrastructure/floors/"
            FormComponent={FloorForm}
            redirectPath="/dashboard/infrastructure/floors"
        />
    );
};

export default AddFloorPage;