import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import ExamTimetableEntryForm
    from '../components/ExamTimetableEntryForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/examTimetableEntryService';

const ExamTimetableEntryCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Exam Timetable Entry"

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

export default ExamTimetableEntryCreatePage;