// ============================================
// EXTRACURRICULAR ACTIVITIES
// ============================================

const extracurricularActivityRoutes = [

    {
        path: 'associations/extracurricular-activities',
        element: <ExtracurricularActivityListPage />,
    },

    {
        path: 'associations/extracurricular-activities/create',
        element: <ExtracurricularActivityCreatePage />,
    },

    {
        path: 'associations/extracurricular-activities/edit/:id',
        element: <ExtracurricularActivityEditPage />,
    },

    {
        path: 'associations/extracurricular-activities/:id',
        element: <ExtracurricularActivityDetailPage />,
    },
];

export default extracurricularActivityRoutes;