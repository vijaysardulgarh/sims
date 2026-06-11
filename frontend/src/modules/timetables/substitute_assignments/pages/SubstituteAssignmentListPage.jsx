import CrudListPage
    from '../../../shared/components/crud/CrudListPage';

import {
    ENDPOINT,
    ADD_PATH,
    EDIT_PATH,
} from '../services/substituteAssignmentService';

const SubstituteAssignmentListPage = () => {

    const columns = [

        {
            key: 'teacher',
            label: 'Absent Teacher',
        },

        {
            key: 'substitute_teacher',
            label: 'Substitute Teacher',
        },

        {
            key: 'timetable_entry',
            label: 'Timetable Entry',
        },

        {
            key: 'assignment_date',
            label: 'Date',
        },

        {
            key: 'reason',
            label: 'Reason',
        },

        {
            key: 'is_active',
            label: 'Active',
        },

    ];

    return (

        <CrudListPage

            title="Substitute Assignments"

            endpoint={ENDPOINT}

            columns={columns}

            addPath={ADD_PATH}

            editPath={EDIT_PATH}

        />

    );

};

export default SubstituteAssignmentListPage;