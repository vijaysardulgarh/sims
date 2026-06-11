import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TimetableVersionForm
    from '../components/TimetableVersionForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableVersionService';

const TimetableVersionCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Timetable Version"

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

export default TimetableVersionCreatePage;