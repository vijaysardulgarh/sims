import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TeacherPreferenceForm
    from '../components/TeacherPreferenceForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/teacherPreferenceService';

const TeacherPreferenceEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Teacher Preference"

            endpoint={ENDPOINT}

            FormComponent={
                TeacherPreferenceForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TeacherPreferenceEditPage;