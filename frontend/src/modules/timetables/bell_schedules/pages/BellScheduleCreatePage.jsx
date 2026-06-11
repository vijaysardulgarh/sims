import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import BellScheduleForm
    from '../components/BellScheduleForm';

import {
    ENDPOINT,
} from '../services/bellScheduleService';

const BellScheduleCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Bell Schedule"

            endpoint={ENDPOINT}

            FormComponent={BellScheduleForm}

            redirectPath="/dashboard/timetables/bell-schedules"

        />

    );

};

export default BellScheduleCreatePage;