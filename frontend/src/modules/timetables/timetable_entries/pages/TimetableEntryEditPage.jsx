import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TimetableEntryForm
    from '../components/TimetableEntryForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableEntryService';

const TimetableEntryEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Timetable Entry"

            endpoint={ENDPOINT}

            FormComponent={
                TimetableEntryForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TimetableEntryEditPage;