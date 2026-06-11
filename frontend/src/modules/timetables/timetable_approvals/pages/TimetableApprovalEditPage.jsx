import CrudEditPage
    from '../../../shared/components/crud/CrudEditPage';

import TimetableApprovalForm
    from '../components/TimetableApprovalForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableApprovalService';

const TimetableApprovalEditPage = () => {

    return (

        <CrudEditPage

            title="Edit Timetable Approval"

            endpoint={ENDPOINT}

            FormComponent={
                TimetableApprovalForm
            }

            redirectPath={
                LIST_PATH
            }

        />

    );

};

export default TimetableApprovalEditPage;