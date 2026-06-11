import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TeacherWorkloadForm
    from '../components/TeacherWorkloadForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/teacherWorkloadService';

const TeacherWorkloadEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Teacher Workload"

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

export default TeacherWorkloadEditPage;