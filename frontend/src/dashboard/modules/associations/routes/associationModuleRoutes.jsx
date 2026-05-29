// ============================================
// ASSOCIATIONS
// ============================================

import associationRoutes from '../associations/routes/associationRoutes';

// ============================================
// ASSOCIATION ROLES
// ============================================

import associationRoleRoutes from '../association_roles/routes/associationRoleRoutes';

// ============================================
// ASSOCIATION MEETINGS
// ============================================

import associationMeetingRoutes from '../association_meetings/routes/associationMeetingRoutes';

// ============================================
// SMC MEMBERS
// ============================================

import smcMemberRoutes from '../smc_members/routes/smcMemberRoutes';
import associationMemberRoutes from '../association_members/routes/associationMemberRoutes';

// ============================================
// ASSOCIATIONS MODULE ROUTES
// ============================================

const associationModuleRoutes = (

    <>

        {/* ================================= */}
        {/* ASSOCIATIONS */}
        {/* ================================= */}

        {associationRoutes}

        {/* ================================= */}
        {/* ASSOCIATION ROLES */}
        {/* ================================= */}

        {associationRoleRoutes}

        {/* ================================= */}
        {/* ASSOCIATION MEETINGS */}
        {/* ================================= */}

        {associationMeetingRoutes}

        {/* ================================= */}
        {/* SMC MEMBERS */}
        {/* ================================= */}

        {smcMemberRoutes}

        {associationMemberRoutes}

    </>
);

// ============================================
// EXPORT
// ============================================

export default associationModuleRoutes;