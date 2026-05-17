import List from "../pages/List";
import Create from "../pages/Create";
import Edit from "../pages/Edit";

const schoolRoutes = [

    {
        path: "schools",
        element: <List />,
    },

    {
        path: "schools/create",
        element: <Create />,
    },

    {
        path: "schools/edit/:id",
        element: <Edit />,
    },
];

export default schoolRoutes;