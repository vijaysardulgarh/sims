import CrudCreatePage
    from '../../../shared/components/crud/CrudCreatePage';

import TimetableApprovalForm
    from '../components/TimetableApprovalForm';

import {
    ENDPOINT,
    LIST_PATH,
} from '../services/timetableApprovalService';

const TimetableApprovalCreatePage = () => {

    return (

        <CrudCreatePage

            title="Create Timetable Approval"

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

export default TimetableApprovalCreatePage;