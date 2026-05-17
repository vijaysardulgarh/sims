import List from "../pages/List";
import Create from "../pages/Create";
import Edit from "../pages/Edit";
import Profile from "../pages/Profile";

const vehicleRoutes = [

    {
        path: "vehicles",
        element: <List />,
    },

    {
        path: "vehicles/create",
        element: <Create />,
    },

    {
        path: "vehicles/edit/:id",
        element: <Edit />,
    },

    {
        path: "vehicles/profile/:id",
        element: <Profile />,
    },
];

export default vehicleRoutes;