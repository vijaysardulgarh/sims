import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import RoomForm from '../components/RoomForm';

const AddRoomPage = () => {

    return (
        <CrudCreatePage
            title="Add Room"
            endpoint="/infrastructure/rooms/"
            FormComponent={RoomForm}
            redirectPath="/dashboard/infrastructure/rooms"
            successMessage="Room created successfully."
        />
    );
};

export default AddRoomPage;