import { Route } from "react-router-dom";

import bellScheduleRoutes
    from "../bell_schedules/routes/bellScheduleRoutes";

import workingDayRoutes
    from "../working_days/routes/workingDayRoutes";

import periodDefinitionRoutes
    from "../period_definitions/routes/periodDefinitionRoutes";

import teacherAvailabilityRoutes
    from "../teacher_availabilities/routes/teacherAvailabilityRoutes";

import teacherPreferenceRoutes
    from "../teacher_preferences/routes/teacherPreferenceRoutes";

import teacherWorkloadRoutes
    from "../teacher_workloads/routes/teacherWorkloadRoutes";

import subjectRequirementRoutes
    from "../subject_requirements/routes/subjectRequirementRoutes";

import subjectConstraintRoutes
    from "../subject_constraints/routes/subjectConstraintRoutes";

import timetableRoutes
    from "../timetables/routes/timetableRoutes";

import timetableEntryRoutes
    from "../timetable_entries/routes/timetableEntryRoutes";

import roomAllocationRoutes
    from "../room_allocations/routes/roomAllocationRoutes";

import resourceAllocationRoutes
    from "../resource_allocations/routes/resourceAllocationRoutes";

import substituteAssignmentRoutes
    from "../substitute_assignments/routes/substituteAssignmentRoutes";

import timetableVersionRoutes
    from "../timetable_versions/routes/timetableVersionRoutes";

import timetableApprovalRoutes
    from "../timetable_approvals/routes/timetableApprovalRoutes";

import timetablePublicationRoutes
    from "../timetable_publications/routes/timetablePublicationRoutes";

import timetableConflictRoutes
    from "../timetable_conflicts/routes/timetableConflictRoutes";

import timetableAuditLogRoutes
    from "../timetable_audit_logs/routes/timetableAuditLogRoutes";

import examTimetableRoutes
    from "../exam_timetables/routes/examTimetableRoutes";

import examTimetableEntryRoutes
    from "../exam_timetable_entries/routes/examTimetableEntryRoutes";

const timetablesRoutes = (

    <Route path="timetables">

        {bellScheduleRoutes}
        {examTimetableRoutes}
        {examTimetableEntryRoutes}

        {workingDayRoutes}

        {periodDefinitionRoutes}

        {teacherAvailabilityRoutes}

        {teacherPreferenceRoutes}

        {teacherWorkloadRoutes}

        {subjectRequirementRoutes}

        {subjectConstraintRoutes}

        {timetableRoutes}

        {timetableEntryRoutes}

        {roomAllocationRoutes}

        {resourceAllocationRoutes}

        {substituteAssignmentRoutes}

        {timetableVersionRoutes}

        {timetableApprovalRoutes}

        {timetablePublicationRoutes}

        {timetableConflictRoutes}

        {timetableAuditLogRoutes}

        

        

    </Route>

);

export default timetablesRoutes;