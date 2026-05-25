// src/modules/accounts/modules/routes/moduleRoutes.jsx

import ModulesListPage from "../pages/ModulesListPage";

import AddModulePage from "../pages/AddModulePage";

import EditModulePage from "../pages/EditModulePage";


const moduleRoutes = [

    {
        path: "/accounts/modules",
        element: <ModulesListPage />,
    },

    {
        path: "/accounts/modules/add",
        element: <AddModulePage />,
    },

    {
        path: "/accounts/modules/:id/edit",
        element: <EditModulePage />,
    },
];

export default moduleRoutes;