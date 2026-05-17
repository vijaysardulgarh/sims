import List from "../pages/List";
import Create from "../pages/Create";
import Edit from "../pages/Edit";
import Profile from "../pages/Profile";


const driverRoutes = [

    {
        path: "drivers",
        element: <List />,
    },

    {
        path: "drivers/create",
        element: <Create />,
    },

    {
        path: "drivers/edit/:id",
        element: <Edit />,
    },

    {
        path: "drivers/profile/:id",
        element: <Profile />,
    },
];

export default driverRoutes;