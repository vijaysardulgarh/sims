// // ============================================
// // ASSOCIATIONS
// // ============================================

// import associationRoutes from '../associations/routes/associationRoutes';

// // // ============================================
// // // ASSOCIATION ROLES
// // // ============================================

// // import associationRoleRoutes from './association_roles/routes/associationRoleRoutes';

// // // ============================================
// // // STAFF ASSOCIATION ROLE ASSIGNMENTS
// // // ============================================

// // import staffRoleAssignmentRoutes from './staff_association_role_assignments/routes/staffRoleAssignmentRoutes';

// // // ============================================
// // // STUDENT ASSOCIATION ROLE ASSIGNMENTS
// // // ============================================

// // import studentRoleAssignmentRoutes from './student_association_role_assignments/routes/studentRoleAssignmentRoutes';

// // // ============================================
// // // ASSOCIATION MEMBERS
// // // ============================================

// // import associationMemberRoutes from './association_members/routes/associationMemberRoutes';

// // // ============================================
// // // ASSOCIATION MEETINGS
// // // ============================================

// // import associationMeetingRoutes from './association_meetings/routes/associationMeetingRoutes';

// // // ============================================
// // // SMC MEMBERS
// // // ============================================

// // import smcMemberRoutes from './smc_members/routes/smcMemberRoutes';

// // // ============================================
// // // EXTRACURRICULAR ACTIVITIES
// // // ============================================

// // import extracurricularActivityRoutes from './extracurricular_activities/routes/extracurricularActivityRoutes';

// // ============================================
// // ASSOCIATIONS MODULE ROUTES
// // ============================================

// const associationModuleRoutes = [

//     ...associationRoutes,
//     // {associationRoleRoutes},
//     // {staffRoleAssignmentRoutes},
//     // {studentRoleAssignmentRoutes},
//     // {associationMemberRoutes},
//     // {associationMeetingRoutes},
//     // {smcMemberRoutes},
//     // {extracurricularActivityRoutes} 
// ];

// // ============================================
// // EXPORT
// // ============================================

// export default associationModuleRoutes;

// ============================================
// ASSOCIATIONS
// ============================================

import associationRoutes from '../associations/routes/associationRoutes';
import smcMemberRoutes from '../smc_members/routes/smcMemberRoutes';
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
        {/* SMC MEMBERS */}
        {/* ================================= */}
        {smcMemberRoutes}

    </>
);

// ============================================
// EXPORT
// ============================================

export default associationModuleRoutes;