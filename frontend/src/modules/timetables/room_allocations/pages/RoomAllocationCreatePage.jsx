import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import RoomAllocationForm
    from '../components/RoomAllocationForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/roomAllocationService';

const RoomAllocationCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Room Allocation"

            endpoint={ENDPOINT}

            FormComponent={
                RoomAllocationForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default RoomAllocationCreatePage;