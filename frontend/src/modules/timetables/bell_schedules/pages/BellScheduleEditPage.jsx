import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import BellScheduleForm
    from '../components/BellScheduleForm';

import {
    ENDPOINT,
} from '../services/bellScheduleService';

const BellScheduleEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Bell Schedule"

            endpoint={ENDPOINT}

            FormComponent={BellScheduleForm}

            redirectPath="/dashboard/timetables/bell-schedules"

        />

    );

};

export default BellScheduleEditPage;