import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TimetableEntryForm
    from '../components/TimetableEntryForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableEntryService';

const TimetableEntryCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Timetable Entry"

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

export default TimetableEntryCreatePage;