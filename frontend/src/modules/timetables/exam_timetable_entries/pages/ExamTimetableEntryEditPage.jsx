import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import ExamTimetableEntryForm
    from '../components/ExamTimetableEntryForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/examTimetableEntryService';

const ExamTimetableEntryEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Exam Timetable Entry"

            endpoint={ENDPOINT}

            FormComponent={
                ExamTimetableEntryForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default ExamTimetableEntryEditPage;