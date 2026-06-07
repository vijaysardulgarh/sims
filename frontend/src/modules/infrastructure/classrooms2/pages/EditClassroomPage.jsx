import CrudEditPage from '../../../shared/components/crud/CrudEditPage';

import ClassroomForm from '../components/ClassroomForm';

const EditClassroomPage = () => {

    return (
        <CrudEditPage
            title="Edit Classroom"
            endpoint="/infrastructure/classrooms/"
            FormComponent={ClassroomForm}
            redirectPath="/dashboard/infrastructure/classrooms"
        />
    );
};

export default EditClassroomPage;