import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TeacherAvailabilityForm
    from '../components/TeacherAvailabilityForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/teacherAvailabilityService';

const TeacherAvailabilityEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Teacher Availability"

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

export default TeacherAvailabilityEditPage;