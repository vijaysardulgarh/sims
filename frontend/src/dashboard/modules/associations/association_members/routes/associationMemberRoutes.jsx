// ============================================
// ASSOCIATION MEMBERS
// ============================================

const associationMemberRoutes = [

    {
        path: 'associations/association-members',
        element: <AssociationMemberListPage />,
    },

    {
        path: 'associations/association-members/create',
        element: <AssociationMemberCreatePage />,
    },

    {
        path: 'associations/association-members/edit/:id',
        element: <AssociationMemberEditPage />,
    },

    {
        path: 'associations/association-members/:id',
        element: <AssociationMemberDetailPage />,
    },
];

export default associationMemberRoutes;