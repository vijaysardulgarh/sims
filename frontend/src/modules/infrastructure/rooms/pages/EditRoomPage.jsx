import CrudEditPage from '../../../../shared/components/common/crud/CrudEditPage';

import RoomForm from '../components/RoomForm';

const EditRoomPage = () => {

    return (

        <CrudEditPage
            title="Edit Room"
            endpoint="/infrastructure/rooms/"
            FormComponent={RoomForm}
            redirectPath="/dashboard/infrastructure/rooms"
        />
    );
};

export default EditRoomPage;