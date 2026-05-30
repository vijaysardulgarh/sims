import {

    useEffect,

    useState

} from "react";

import {

    useNavigate,

    useParams

} from "react-router-dom";

import RoleForm from "../components/RoleForm";

import roleService from "../services/roleService";


const EditRolePage = () => {

    const { id } = useParams();

    const navigate = useNavigate();

    const [role, setRole] = useState(null);

    const [loading, setLoading] = useState(true);


    // =====================================
    // FETCH ROLE
    // =====================================

    useEffect(() => {

        fetchRole();

    }, []);


    const fetchRole = async () => {

        try {

            const data = await roleService.getRole(
                id
            );

            setRole(data);

        } catch (error) {

            console.error(
                "Fetch Role Error:",
                error
            );

        } finally {

            setLoading(false);
        }
    };


    // =====================================
    // UPDATE ROLE
    // =====================================

    const handleSubmit = async (
        formData
    ) => {

        try {

            await roleService.updateRole(

                id,

                formData
            );

            navigate(
                "/dashboard/roles"
            );

        } catch (error) {

            console.error(
                "Update Role Error:",
                error
            );
        }
    };


    if (loading) {

        return <p>Loading...</p>;
    }


    return (

        <div className="p-4">

            <h1 className="text-2xl font-bold mb-4">

                Edit Role

            </h1>

            <RoleForm

                initialData={role}

                onSubmit={handleSubmit}
            />

        </div>
    );
};

export default EditRolePage;