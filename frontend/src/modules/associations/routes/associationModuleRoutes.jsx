import associationRoutes from '../associations/routes/associationRoutes';

import associationRoleRoutes from '../association-roles/routes/associationRoleRoutes';

import associationRoleAssignmentRoutes from '../association-role-assignments/routes/associationRoleAssignmentRoutes';

import associationMeetingRoutes from '../association-meetings/routes/associationMeetingRoutes';

import associationMemberRoutes from '../association-members/routes/associationMemberRoutes';

import smcMemberRoutes from '../smc-members/routes/smcMemberRoutes';

import extracurricularActivityRoutes from '../extracurricular-activities/routes/extracurricularActivityRoutes';

const associationModuleRoutes = (

    <>

        {associationRoutes}

        {associationRoleRoutes}

        {associationMeetingRoutes}

        {associationRoleAssignmentRoutes}

        {associationMemberRoutes}

        {smcMemberRoutes}

        {extracurricularActivityRoutes}

    </>

);

export default associationModuleRoutes;