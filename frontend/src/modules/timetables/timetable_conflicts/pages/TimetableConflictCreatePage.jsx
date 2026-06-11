import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TimetableConflictForm
    from '../components/TimetableConflictForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableConflictService';

const TimetableConflictCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Timetable Conflict"

            endpoint={ENDPOINT}

            FormComponent={
                TimetableConflictForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TimetableConflictCreatePage;