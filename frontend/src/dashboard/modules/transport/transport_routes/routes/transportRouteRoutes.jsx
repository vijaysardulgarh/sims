import List from "../pages/List";
import Create from "../pages/Create";
import Edit from "../pages/Edit";
import Profile from "../pages/Profile";


const transportRouteRoutes = [

    {
        path: "transport-routes",
        element: <List />,
    },

    {
        path: "transport-routes/create",
        element: <Create />,
    },

    {
        path: "transport-routes/edit/:id",
        element: <Edit />,
    },

    {
        path: "transport-routes/profile/:id",
        element: <Profile />,
    },
];

export default transportRouteRoutes;