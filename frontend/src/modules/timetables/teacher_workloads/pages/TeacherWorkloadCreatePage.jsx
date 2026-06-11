import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TeacherWorkloadForm
    from '../components/TeacherWorkloadForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/teacherWorkloadService';

const TeacherWorkloadCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Teacher Workload"

            endpoint={ENDPOINT}

            FormComponent={
                TeacherWorkloadForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TeacherWorkloadCreatePage;