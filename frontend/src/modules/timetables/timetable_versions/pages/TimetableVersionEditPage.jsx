import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TimetableVersionForm
    from '../components/TimetableVersionForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableVersionService';

const TimetableVersionEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Timetable Version"

            endpoint={ENDPOINT}

            FormComponent={
                TimetableVersionForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TimetableVersionEditPage;