import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import ResourceAllocationForm
    from '../components/ResourceAllocationForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/resourceAllocationService';

const ResourceAllocationCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Resource Allocation"

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

export default ResourceAllocationCreatePage;