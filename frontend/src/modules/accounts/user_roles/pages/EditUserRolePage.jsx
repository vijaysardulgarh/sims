import {

    useEffect,

    useState

} from "react";

import {

    useNavigate,

    useParams

} from "react-router-dom";

import UserRoleForm from "../components/UserRoleForm";

import userRoleService from "../services/userRoleService";

import userService from "../../users/services/userService";

import roleService from "../../roles/services/roleService";


const EditUserRolePage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [initialData, setInitialData] =
        useState(null);

    const [users, setUsers] =
        useState([]);

    const [roles, setRoles] =
        useState([]);


    // =====================================
    // FETCH
    // =====================================

    useEffect(() => {

        fetchUserRole();

        fetchUsers();

        fetchRoles();

    }, []);


    const fetchUserRole = async () => {

        try {

            const data =
                await userRoleService.getUserRole(id);

            setInitialData(data);

        } catch (error) {

            console.error(error);
        }
    };


    const fetchUsers = async () => {

        try {

            const data =
                await userService.getUsers();

            setUsers(data);

        } catch (error) {

            console.error(error);
        }
    };


    const fetchRoles = async () => {

        try {

            const data =
                await roleService.getRoles();

            setRoles(data);

        } catch (error) {

            console.error(error);
        }
    };


    // =====================================
    // UPDATE
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            await userRoleService.updateUserRole(

                id,

                formData
            );

            navigate(
                "/dashboard/user-roles"
            );

        } catch (error) {

            console.error(error);
        }
    };


    if (!initialData) {

        return <p>Loading...</p>;
    }


    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">

                Edit User Role

            </h1>

            <UserRoleForm

                initialData={initialData}

                users={users}

                roles={roles}

                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default EditUserRolePage;