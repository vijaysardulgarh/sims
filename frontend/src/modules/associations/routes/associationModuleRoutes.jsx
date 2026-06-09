import associationRoutes from '../associations/routes/associationRoutes';

import associationRoleRoutes from '../association-roles/routes/associationRoleRoutes';

import associationRoleAssignmentRoutes from '../association-role-assignments/routes/associationRoleAssignmentRoutes';
import associationMeetingRoutes from '../association-meetings/routes/associationMeetingRoutes';

import smcMemberRoutes from '../smc-members/routes/smcMemberRoutes';

import associationMemberRoutes from '../association-members/routes/associationMemberRoutes';


const associationModuleRoutes = (

    <>

        {associationRoutes}

        {associationRoleRoutes}

        {associationMeetingRoutes}

        {associationRoleAssignmentRoutes}

        {smcMemberRoutes}

        {associationMemberRoutes}

    </>

);

export default associationModuleRoutes;