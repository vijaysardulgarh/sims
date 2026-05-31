import CrudCreatePage from '../../../../components/common/crud/CrudCreatePage';

import RoomForm from '../components/RoomForm';

const AddRoomPage = () => {

    return (

        <CrudCreatePage
            title="Add Room"
            endpoint="/infrastructure/rooms/"
            FormComponent={RoomForm}
            redirectPath="/dashboard/infrastructure/rooms"
        />
    );
};

export default AddRoomPage;