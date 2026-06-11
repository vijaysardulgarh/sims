import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import RoomAllocationForm
    from '../components/RoomAllocationForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/roomAllocationService';

const RoomAllocationEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Room Allocation"

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

export default RoomAllocationEditPage;