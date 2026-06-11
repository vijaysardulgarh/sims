import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import PeriodDefinitionForm
    from '../components/PeriodDefinitionForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/periodDefinitionService';

const PeriodDefinitionEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Period Definition"

            endpoint={ENDPOINT}

            FormComponent={
                PeriodDefinitionForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default PeriodDefinitionEditPage;