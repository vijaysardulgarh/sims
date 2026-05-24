import {

    useEffect,

    useState

} from "react";

import {

    useNavigate

} from "react-router-dom";

import UserRoleForm from "../UserRoleForm";

import userRoleService from "../../services/userRoleService";

import userService from "../../services/userService";

import roleService from "../../services/roleService";


const AddUserRolePage = () => {

    const navigate = useNavigate();

    const [users, setUsers] =
        useState([]);

    const [roles, setRoles] =
        useState([]);


    // =====================================
    // FETCH DATA
    // =====================================

    useEffect(() => {

        fetchUsers();

        fetchRoles();

    }, []);


    // =====================================
    // FETCH USERS
    // =====================================

    const fetchUsers = async () => {

        try {

            const data =
                await userService.getUsers();

            console.log(
                "Users:",
                data
            );

            setUsers(
                data.results || data
            );

        } catch (error) {

            console.error(
                "Fetch Users Error:",
                error
            );
        }
    };


    // =====================================
    // FETCH ROLES
    // =====================================

    const fetchRoles = async () => {

        try {

            const data =
                await roleService.getRoles();

            console.log(
                "Roles:",
                data
            );

            setRoles(
                data.results || data
            );

        } catch (error) {

            console.error(
                "Fetch Roles Error:",
                error
            );
        }
    };


    // =====================================
    // CREATE USER ROLE
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            await userRoleService.createUserRole(
                formData
            );

            navigate(
                "/dashboard/user-roles"
            );

        } catch (error) {

            console.error(
                "Create User Role Error:",
                error
            );
        }
    };


    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">

                Add User Role

            </h1>

            <UserRoleForm

                users={users}

                roles={roles}

                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default AddUserRolePage;