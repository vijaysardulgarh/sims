// ============================================
// ASSOCIATION MEETINGS
// ============================================

const associationMeetingRoutes = [

    {
        path: 'associations/association-meetings',
        element: <AssociationMeetingListPage />,
    },

    {
        path: 'associations/association-meetings/create',
        element: <AssociationMeetingCreatePage />,
    },

    {
        path: 'associations/association-meetings/edit/:id',
        element: <AssociationMeetingEditPage />,
    },

    {
        path: 'associations/association-meetings/:id',
        element: <AssociationMeetingDetailPage />,
    },
];

export default associationMeetingRoutes;