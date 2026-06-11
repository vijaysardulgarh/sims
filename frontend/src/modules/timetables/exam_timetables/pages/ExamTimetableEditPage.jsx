import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import ExamTimetableForm
    from '../components/ExamTimetableForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/examTimetableService';

const ExamTimetableEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Exam Timetable"

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

export default ExamTimetableEditPage;