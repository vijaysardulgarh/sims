import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TimetableForm
    from '../components/TimetableForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableService';

const TimetableEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Timetable"

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

export default TimetableEditPage;