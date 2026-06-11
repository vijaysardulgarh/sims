import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TimetableForm
    from '../components/TimetableForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableService';

const TimetableCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Timetable"

            endpoint={ENDPOINT}

            FormComponent={
                TimetableForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TimetableCreatePage;