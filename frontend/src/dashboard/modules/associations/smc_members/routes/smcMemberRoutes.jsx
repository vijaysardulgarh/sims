// ============================================
// SMC MEMBERS
// ============================================

const smcMemberRoutes = [

    {
        path: 'associations/smc-members',
        element: <SmcMemberListPage />,
    },

    {
        path: 'associations/smc-members/create',
        element: <SmcMemberCreatePage />,
    },

    {
        path: 'associations/smc-members/edit/:id',
        element: <SmcMemberEditPage />,
    },

    {
        path: 'associations/smc-members/:id',
        element: <SmcMemberDetailPage />,
    },
];

export default smcMemberRoutes;