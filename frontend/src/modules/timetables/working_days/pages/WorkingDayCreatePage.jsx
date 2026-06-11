import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import WorkingDayForm
    from '../components/WorkingDayForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/workingDayService';

const WorkingDayCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Working Day"

            endpoint={ENDPOINT}

            FormComponent={
                WorkingDayForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default WorkingDayCreatePage;