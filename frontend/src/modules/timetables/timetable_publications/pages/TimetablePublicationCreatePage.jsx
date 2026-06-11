import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TimetablePublicationForm
    from '../components/TimetablePublicationForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetablePublicationService';

const TimetablePublicationCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Timetable Publication"

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

export default TimetablePublicationCreatePage;