import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import ResourceAllocationForm
    from '../components/ResourceAllocationForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/resourceAllocationService';

const ResourceAllocationEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Resource Allocation"

            endpoint={ENDPOINT}

            FormComponent={
                ResourceAllocationForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default ResourceAllocationEditPage;