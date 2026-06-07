import CrudCreatePage from '../../../shared/components/crud/CrudCreatePage';

import ClassroomForm from '../components/ClassroomForm';

const AddClassroomPage = () => {

    return (
        <CrudCreatePage
            title="Add Classroom"
            endpoint="/infrastructure/classrooms/"
            FormComponent={ClassroomForm}
            redirectPath="/dashboard/infrastructure/classrooms"
        />
    );
};

export default AddClassroomPage;