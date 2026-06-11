import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import PeriodDefinitionForm
    from '../components/PeriodDefinitionForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/periodDefinitionService';

const PeriodDefinitionCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Period Definition"

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

export default PeriodDefinitionCreatePage;