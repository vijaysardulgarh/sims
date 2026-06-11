import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TimetableConflictForm
    from '../components/TimetableConflictForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableConflictService';

const TimetableConflictEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Timetable Conflict"

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

export default TimetableConflictEditPage;