import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TeacherAvailabilityForm
    from '../components/TeacherAvailabilityForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/teacherAvailabilityService';

const TeacherAvailabilityCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Teacher Availability"

            endpoint={ENDPOINT}

            FormComponent={
                TeacherAvailabilityForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TeacherAvailabilityCreatePage;