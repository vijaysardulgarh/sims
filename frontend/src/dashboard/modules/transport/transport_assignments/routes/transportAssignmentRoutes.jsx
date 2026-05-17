import List from "../pages/List";
import Create from "../pages/Create";
import Edit from "../pages/Edit";
import Profile from "../pages/Profile";


const transportAssignmentRoutes = [

    {
        path: "transport-assignments",
        element: <List />,
    },

    {
        path: "transport-assignments/create",
        element: <Create />,
    },

    {
        path: "transport-assignments/edit/:id",
        element: <Edit />,
    },

    {
        path: "transport-assignments/profile/:id",
        element: <Profile />,
    },
];

export default transportAssignmentRoutes;