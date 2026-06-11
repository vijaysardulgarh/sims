import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TimetablePublicationForm
    from '../components/TimetablePublicationForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetablePublicationService';

const TimetablePublicationEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Timetable Publication"

            endpoint={ENDPOINT}

            FormComponent={
                TimetablePublicationForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TimetablePublicationEditPage;