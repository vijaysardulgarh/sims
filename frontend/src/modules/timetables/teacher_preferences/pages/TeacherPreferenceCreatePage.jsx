import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TeacherPreferenceForm
    from '../components/TeacherPreferenceForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/teacherPreferenceService';

const TeacherPreferenceCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Teacher Preference"

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

export default TeacherPreferenceCreatePage;