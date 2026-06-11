import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import ExamTimetableForm
    from '../components/ExamTimetableForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/examTimetableService';

const ExamTimetableCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Exam Timetable"

            endpoint={ENDPOINT}

            FormComponent={
                ExamTimetableForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default ExamTimetableCreatePage;