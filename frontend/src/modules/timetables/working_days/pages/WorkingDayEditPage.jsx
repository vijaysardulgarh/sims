import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import WorkingDayForm
    from '../components/WorkingDayForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/workingDayService';

const WorkingDayEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Working Day"

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

export default WorkingDayEditPage;